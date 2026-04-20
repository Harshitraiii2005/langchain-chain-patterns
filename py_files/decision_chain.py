from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnablePassthrough
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal
import io
import sys

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative", "neutral"] = Field(description="The sentiment of the feedback")

parser = PydanticOutputParser(pydantic_object=Feedback)
text_parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback:\n{feedback}\n\n{format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="Generate a response to this positive feedback:\n{feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="Generate a response to this negative feedback:\n{feedback}",
    input_variables=["feedback"]
)

prompt4 = PromptTemplate(
    template="Generate a response to this neutral feedback:\n{feedback}",
    input_variables=["feedback"]
)

classifier_chain = prompt1 | model | parser

chain = (
    RunnablePassthrough.assign(sentiment=classifier_chain)
    | RunnableLambda(lambda x: {"feedback": x["feedback"], "sentiment": x["sentiment"].sentiment})
    | RunnableBranch(
        (lambda x: x["sentiment"] == "positive", prompt2 | model | text_parser),
        (lambda x: x["sentiment"] == "negative", prompt3 | model | text_parser),
        (lambda x: x["sentiment"] == "neutral", prompt4 | model | text_parser),
        RunnableLambda(lambda x: f"Unhandled sentiment: {x['sentiment']}")
    )
)

result = chain.invoke({"feedback": "I love this product!"})

buffer = io.StringIO()
sys_stdout = sys.stdout
sys.stdout = buffer

chain.get_graph().print_ascii()

sys.stdout = sys_stdout
graph = buffer.getvalue()

formatted_output = f"""
===== GRAPH =====
{graph}

===== RESULT =====
{result}
"""

with open("decision_result.txt", "w") as f:
    f.write(formatted_output)

print("Saved successfully")