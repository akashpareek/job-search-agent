<<<<<<< HEAD
import streamlit as st

from agent_setup import agent

st.title("AI Job Search Agent")

query = st.text_input(
    "Enter your job search query"
)

if st.button("Search"):

    response = agent.invoke({"input": query})

=======
import streamlit as st

from agent_setup import agent

st.title("AI Job Search Agent")

query = st.text_input(
    "Enter your job search query"
)

if st.button("Search"):

    response = agent.invoke({"input": query})

>>>>>>> 918364ee7a86bc7abedc5f8966278f47ba43336d
    st.write(response["output"])