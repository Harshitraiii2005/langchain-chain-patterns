from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(
    model= "openai/gpt-oss-120b",
)

prompt1 = PromptTemplate(
    template = "You are a expert reveiwer and generate a detailed review of the following text: {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

template = prompt1.invoke({"text":"popularity of cricket in india"})
result = model.invoke(template)

final_result = parser.invoke(result)
print(final_result)

with open('traditional_result.txt', 'w') as f:
    f.write("before applying the parser the raw output \n")
    f.write(str(result))
    f.write("after applying the parser the result \n")
    f.write(str(final_result))