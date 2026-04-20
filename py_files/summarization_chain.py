from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import io
import sys

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")
parser = StrOutputParser()

document = """
Artificial Intelligence (AI) has become one of the most transformative technologies of our time. 
It encompasses a wide range of capabilities including machine learning, natural language processing, 
computer vision, and robotics. AI is being used in various industries such as healthcare, finance, 
manufacturing, and entertainment. In healthcare, AI is helping doctors diagnose diseases more accurately 
and quickly. In finance, it's being used for fraud detection and algorithmic trading. In manufacturing, 
AI powers automation and quality control. The potential applications of AI are virtually limitless, 
but so are the ethical considerations we must address. Privacy, bias, accountability, and job displacement 
are all critical concerns as we continue to develop and deploy AI systems. Educational institutions are 
increasingly focusing on AI literacy and ethics in their curricula. The future of AI lies not just in 
technological advancement but in ensuring these systems are developed and used responsibly for the benefit of humanity.
"""

abstract_summary_prompt = PromptTemplate(
    template="Provide a 2-3 sentence abstract summary of the following text:\n\n{text}",
    input_variables=["text"]
)

detailed_summary_prompt = PromptTemplate(
    template="Provide a detailed summary (5-7 sentences) covering all key points of the following text:\n\n{text}",
    input_variables=["text"]
)

bullet_point_prompt = PromptTemplate(
    template="Extract and list the main key points from the following text as bullet points:\n\n{text}",
    input_variables=["text"]
)

abstract_chain = abstract_summary_prompt | model | parser
detailed_chain = detailed_summary_prompt | model | parser
bullet_chain = bullet_point_prompt | model | parser

buffer = io.StringIO()
sys_stdout = sys.stdout
sys.stdout = buffer

abstract_chain.get_graph().print_ascii()

sys.stdout = sys_stdout
graph = buffer.getvalue()

results_output = "===== SUMMARIZATION CHAIN GRAPH =====\n"
results_output += graph
results_output += "\n\n===== ORIGINAL DOCUMENT =====\n"
results_output += document
results_output += "\n\n===== ABSTRACT SUMMARY =====\n"

abstract_result = abstract_chain.invoke({"text": document})
results_output += abstract_result

results_output += "\n\n===== DETAILED SUMMARY =====\n"
detailed_result = detailed_chain.invoke({"text": document})
results_output += detailed_result

results_output += "\n\n===== KEY POINTS =====\n"
bullet_result = bullet_chain.invoke({"text": document})
results_output += bullet_result

print(results_output)

with open("../results/summarization_result.txt", "w") as f:
    f.write(results_output)

print("Summarization Chain execution completed. Results saved to ../results/summarization_result.txt")
