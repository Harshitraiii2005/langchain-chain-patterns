from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import io
import sys

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")
parser = StrOutputParser()

context = """
Machine Learning is a subset of Artificial Intelligence that enables systems to learn and improve 
from experience without being explicitly programmed. Machine Learning focuses on the development 
of computer programs that can access data and learn from it autonomously. The process of learning 
begins with observations or data such as examples, direct experience, or instruction. Machine Learning 
algorithms build a mathematical model based on sample data, known as training data, in order to make 
predictions or decisions without being explicitly programmed to perform the task.
"""

qa_prompt = PromptTemplate(
    template="""You are a helpful assistant. Answer the following question based on the provided context.
    
Context: {context}

Question: {question}

Provide a detailed and accurate answer:""",
    input_variables=["context", "question"]
)

qa_chain = qa_prompt | model | parser


questions = [
    "What is Machine Learning?",
    "How does Machine Learning differ from traditional programming?",
    "What is training data in Machine Learning?"
]


buffer = io.StringIO()
sys_stdout = sys.stdout
sys.stdout = buffer

qa_chain.get_graph().print_ascii()

sys.stdout = sys_stdout
graph = buffer.getvalue()


results_output = "===== Q&A CHAIN GRAPH =====\n"
results_output += graph
results_output += "\n\n===== Q&A RESULTS =====\n"

for question in questions:
    result = qa_chain.invoke({"context": context, "question": question})
    results_output += f"\nQuestion: {question}\n"
    results_output += f"Answer: {result}\n"
    results_output += "-" * 80 + "\n"

print(results_output)


with open("../results/qa_result.txt", "w") as f:
    f.write(results_output)

print("Q&A Chain execution completed. Results saved to ../results/qa_result.txt")
