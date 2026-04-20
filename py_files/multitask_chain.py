from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import io
import sys

load_dotenv()

prompt1 = PromptTemplate(
    template="you are a writer write one paragraph on the following topic: {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="you are an expert reviewer and given one para generate a detailed review, summary, and 2-3 key points: {paragraph}",
    input_variables=["paragraph"]
)

prompt3 = PromptTemplate(
    template="you are a college teacher and evaluate the following paragraph and give feedback: {paragraph}",
    input_variables=["paragraph"]
)

model = ChatGroq(model="openai/gpt-oss-120b")
parser = StrOutputParser()

chains = (
    prompt1
    | model
    | parser
    | (lambda x: {"paragraph": x})
    | prompt2
    | model
    | parser
    | (lambda x: {"paragraph": x})
    | prompt3
    | model
    | parser
)


buffer = io.StringIO()
sys_stdout = sys.stdout
sys.stdout = buffer

chains.get_graph().print_ascii()

sys.stdout = sys_stdout
graph = buffer.getvalue()


result = chains.invoke({"topic": "Rise of AI"})


with open("multitask_result.txt", "w") as f:
    f.write("===== GRAPH =====\n")
    f.write(graph)
    f.write("\n\n===== RESULT =====\n")
    f.write(result)

print("Saved successfully")