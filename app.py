import streamlit as st

from agent_setup import agent

st.title("AI Job Search Agent")

query = st.text_input(
    "Enter your job search query"
)

if st.button("Search"):

    response = agent.invoke({"input": query})

    st.write(response["output"])