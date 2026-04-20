from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import io
import sys

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

prompt1 = PromptTemplate(
    template="You are an expert reviewer and generate a detailed review of the following text: {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chains = prompt1 | model | parser


buffer = io.StringIO()
sys_stdout = sys.stdout
sys.stdout = buffer

chains.get_graph().print_ascii()

sys.stdout = sys_stdout
graph = buffer.getvalue()


chain_result = chains.invoke({"text": "popularity of cricket in india"})


with open("sequential_result.txt", "w") as f:
    f.write(" CHAIN GRAPH\n")
    f.write(graph)

    f.write("\n\nRESULT \n")
    f.write(chain_result)
