from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import io
import sys

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")
parser = StrOutputParser()


prompt = PromptTemplate(
    template="""You are a helpful AI assistant. You maintain a conversation with the user.
    
Previous conversation history:
{history}

Current user input: {input}

Please provide a helpful response:""",
    input_variables=["history", "input"]
)


conversation_history = []

def format_history():
    """Format conversation history as string"""
    if not conversation_history:
        return "No previous conversation."
    
    history_text = ""
    for i, msg in enumerate(conversation_history):
        if i % 2 == 0:
            history_text += f"User: {msg}\n"
        else:
            history_text += f"Assistant: {msg}\n"
    return history_text


conversation_chain = prompt | model | parser


user_inputs = [
    "Hello! What is Python?",
    "Can you tell me about its applications?",
    "How can I learn Python effectively?",
]

buffer = io.StringIO()
sys_stdout = sys.stdout
sys.stdout = buffer

conversation_chain.get_graph().print_ascii()

sys.stdout = sys_stdout
graph = buffer.getvalue()


results_output = "===== MEMORY/CONVERSATION CHAIN GRAPH =====\n"
results_output += graph
results_output += "\n\n===== CONVERSATION HISTORY =====\n"

for user_input in user_inputs:
    response = conversation_chain.invoke({
        "history": format_history(),
        "input": user_input
    })
    
    conversation_history.append(user_input)
    conversation_history.append(response)
    
    results_output += f"\nUser: {user_input}\n"
    results_output += f"Assistant: {response}\n"
    results_output += "-" * 80 + "\n"

print(results_output)


with open("../results/memory_result.txt", "w") as f:
    f.write(results_output)

print("Memory/Conversation Chain execution completed. Results saved to ../results/memory_result.txt")
