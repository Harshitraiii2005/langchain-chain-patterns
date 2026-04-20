from langchain_core.tools import tool
from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq

model = ChatGroq(model="openai/gpt-oss-120b")
@tool
def multiply(a: int, b: int) -> int:
    return a * b

tools = [multiply]

agent = initialize_agent(
    tools,
    model,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

result = agent.invoke("What is 5 multiplied by 6?")
print(result)