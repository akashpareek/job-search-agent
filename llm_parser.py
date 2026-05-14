from langchain_groq import ChatGroq
from dotenv import load_dotenv
import json

load_dotenv()

llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=200
)


def parse_user_query(user_query):

    prompt = f"""
You are an AI system that extracts structured job search information.

Rules:
1. Determine if the query is related to jobs/careers/employment.
2. Return ONLY valid JSON.
3. Do NOT add explanations.
4. Always return all fields.

JSON format:

{{
    "is_job_query": true,
    "role": "",
    "location": "",
    "experience": "",
    "remote": false
}}

Examples:

Query:
Find Android developer jobs in Bangalore with 3 years experience

Output:
{{
    "is_job_query": true,
    "role": "Android Developer",
    "location": "Bangalore",
    "experience": "3",
    "remote": false
}}

Query:
Who won IPL yesterday

Output:
{{
    "is_job_query": false,
    "role": "",
    "location": "",
    "experience": "",
    "remote": false
}}

Now process this query:

{user_query}
"""

    response = llm.invoke(prompt)

    content = response.content.strip()

    print(content)

    try:
        return json.loads(content)

    except Exception as e:

        print("JSON ERROR:", e)

        return {
            "is_job_query": False,
            "role": "",
            "location": "",
            "experience": "",
            "remote": False
        }