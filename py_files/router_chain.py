from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
import io
import sys

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")
parser = StrOutputParser()

prompt_explain = PromptTemplate(
    template="Explain the topic: {topic}",
    input_variables=["topic"]
)

prompt_mcq = PromptTemplate(
    template="Generate 5 MCQs on: {topic}",
    input_variables=["topic"]
)

def router(x):
    if "mcq" in x["topic"].lower():
        return prompt_mcq | model | parser
    return prompt_explain | model | parser

chain = RunnableLambda(router)

result = chain.invoke({"topic": "generate mcq on AI"})

buffer = io.StringIO()
sys_stdout = sys.stdout
sys.stdout = buffer

chain.get_graph().print_ascii()

sys.stdout = sys_stdout
graph = buffer.getvalue()

formatted_output = f"""
===== ROUTER CHAIN GRAPH =====
{graph}

===== RESULT =====
{result}
"""

with open("router_result.txt", "w") as f:
    f.write(formatted_output)

print("saved successfully")