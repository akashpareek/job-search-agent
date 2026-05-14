from textblob import TextBlob
import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPID_API_KEY = os.getenv("RAPID_API_KEY")

# manual city typo fixes
CITY_FIXES = {
    "banglore": "Bangalore",
    "hydrabad": "Hyderabad",
    "punee": "Pune",
    "delhii": "Delhi"
}


def clean_text(text):

    if not text:
        return ""

    corrected = str(
        TextBlob(text).correct()
    )

    corrected_lower = corrected.lower()

    if corrected_lower in CITY_FIXES:
        return CITY_FIXES[corrected_lower]

    return corrected


def search_jobs(role, location, experience, remote):

    role = clean_text(role)

    location = clean_text(location)

    query_parts = []

    if role:
        query_parts.append(role)

    if location:
        query_parts.append(location)

    if remote:
        query_parts.append("remote")

    # IMPORTANT:
    # experience intentionally removed
    # from primary search query

    query = " ".join(query_parts)

    print("FINAL API QUERY:", query)

    url = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    params = {
        "query": query,
        "page": "1",
        "num_pages": "1"
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    data = response.json()

    jobs = data.get("data", [])

    # fallback retry
    if not jobs:

        fallback_query = (
            f"{role} jobs in {location}"
        )

        print(
            "FALLBACK QUERY:",
            fallback_query
        )

        params["query"] = fallback_query

        response = requests.get(
            url,
            headers=headers,
            params=params
        )

        data = response.json()

        jobs = data.get("data", [])

    # EXPERIENCE FILTERING
    if experience:

        filtered_jobs = []

        for job in jobs:

            description = str(
                job.get(
                    "job_description",
                    ""
                )
            ).lower()

            title = str(
                job.get(
                    "job_title",
                    ""
                )
            ).lower()

            exp_text = str(experience)

            if (
                exp_text in description
                or exp_text in title
                or "senior" in description
                or "mid" in description
                or "lead" in description
            ):

                filtered_jobs.append(job)

        # only replace if filtered jobs exist
        if filtered_jobs:

            data["data"] = filtered_jobs

    return data