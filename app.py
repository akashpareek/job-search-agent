import streamlit as st

from agent_tools import search_jobs

st.title("AI Job Search Agent")

query = st.text_input(
    "Enter your job search query"
)

if st.button("Search"):

    response = search_jobs.invoke(query)

    st.write(response)