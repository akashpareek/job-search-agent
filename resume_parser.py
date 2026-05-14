from pypdf import PdfReader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import json

load_dotenv()

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=300
)


def extract_resume_text(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text



def analyze_resume(resume_text):

    prompt = f"""
You are an AI resume analyzer.

Extract the following information from the resume.

Return ONLY valid JSON.

JSON format:

{{
    "job_title": "",
    "years_of_experience": "",
    "last_location": "",
    "skills": []
}}

Resume:
{resume_text}
"""

    response = llm.invoke(prompt)

    content = response.content.strip()

    print(content)

    try:
        return json.loads(content)

    except:

        return {
            "job_title": "",
            "years_of_experience": "",
            "last_location": "",
            "skills": []
        }