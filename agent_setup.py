from langchain.agents import initialize_agent
from langchain.agents import AgentType

from langchain_groq import ChatGroq

from agent_tools import search_jobs,experience_filter
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()


llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=300
)

tools = [search_jobs,experience_filter]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    memory=memory,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
max_iterations=3,
    early_stopping_method="generate"
)