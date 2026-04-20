from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
import io
import sys

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="generate a report on the given topic: {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="generate 10 mcq on the given topic: {topic}",
    input_variables=["topic"]
)

prompt3 = PromptTemplate(
    template="explain this topic like a teacher: {topic}",
    input_variables=["topic"]
)


chain = RunnableParallel(
    explanation=prompt3 | model | parser,
    report=prompt1 | model | parser,
    mcq=prompt2 | model | parser
)

result = chain.invoke({"topic": "Machine Learning"})

buffer = io.StringIO()
sys_stdout = sys.stdout
sys.stdout = buffer

chain.get_graph().print_ascii()

sys.stdout = sys_stdout
graph = buffer.getvalue()


with open("parallel_result.txt", "w") as f:
    f.write(" CHAIN GRAPH \n")
    f.write(graph)

    f.write("\n\n RESULTS \n")

    f.write("\n\n TEACHER EXPLANATION\n")
    f.write(result["explanation"])

    f.write("\n\nREPORT \n")
    f.write(result["report"])

    f.write("\n\nMCQs\n")
    f.write(result["mcq"])

