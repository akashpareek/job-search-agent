import streamlit as st

from llm_parser import parse_user_query
from api_service import search_jobs
from response_formatter import format_jobs
from resume_parser import (
    extract_resume_text,
    analyze_resume
)

st.title("AI Job Search Agent")

mode = st.radio(
    "Choose Search Mode",
    [
        "Manual Query",
        "Resume Based"
    ]
)


# MANUAL SEARCH
if mode == "Manual Query":

    query = st.text_input(
        "Enter your query"
    )

    if st.button("Search Jobs"):

        parsed = parse_user_query(query)

        print(parsed)

        if not parsed["is_job_query"]:

            st.error(
                "Query is not related to jobs"
            )

        else:

            data = search_jobs(
                parsed["role"],
                parsed["location"],
                parsed["experience"],
                parsed["remote"]
            )

            result = format_jobs(data)

            st.write(result)


# RESUME SEARCH
if mode == "Resume Based":

    uploaded_file = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    if uploaded_file:

        with open("temp_resume.pdf", "wb") as f:
            f.write(uploaded_file.read())

        resume_text = extract_resume_text(
            "temp_resume.pdf"
        )

        parsed_resume = analyze_resume(
            resume_text
        )

        st.subheader("Extracted Resume Details")

        st.json(parsed_resume)

        if st.button("Find Relevant Jobs"):

            data = search_jobs(
                parsed_resume["job_title"],
                parsed_resume["last_location"],
                parsed_resume["years_of_experience"],
                False
            )

            result = format_jobs(data)

            st.subheader("Recommended Jobs")

            st.write(result)