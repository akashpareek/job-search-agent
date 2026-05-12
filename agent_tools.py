from langchain.tools import tool
import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPID_API_KEY = os.getenv("RAPID_API_KEY")



@tool
def search_jobs(query: str):
    """
    Search jobs from API based on query.
    """

    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {
        "query": query,
        "page": "1",
        "num_pages": "1"
    }

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(
        url,
        headers=headers,
        params=querystring
    )

    data = response.json()

    jobs = data.get("data", [])

    results = []

    for job in jobs[:5]:

        results.append(
            f"""
Company: {job.get('employer_name')}

Role: {job.get('job_title')}

Location: {job.get('job_city')}

Apply Link:
{job.get('job_apply_link')}
"""
        )

    return "\n\n".join(results)

@tool
def experience_filter(text: str):
    """
    Filters jobs suitable for 3 years experience.
    """

    lines = text.split("\n")

    filtered = []

    for line in lines:

        if "3" in line or "2" in line:

            filtered.append(line)

    return "\n".join(filtered)