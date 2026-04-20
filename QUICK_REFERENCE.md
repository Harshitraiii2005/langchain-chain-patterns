# Quick Reference Guide - LangChain Chains

**Written by Harshit**

---

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r py_files/requirements.txt

# Run a specific chain
cd py_files
python sequential_chain.py

# View results
cd ../results
cat sequential_result.txt
```

---

## 📊 Chain Comparison Table

| Chain Type | Complexity | Use Case | Speed | Output |
|-----------|-----------|----------|-------|--------|
| **Traditional** | ⭐ | Basic prompting | 🚀 Fast | Single |
| **Sequential** | ⭐⭐ | Step-by-step processing | 🚀 Fast | Single |
| **Parallel** | ⭐⭐ | Multiple independent tasks | ⚡ Very Fast | Multiple |
| **Router** | ⭐⭐⭐ | Conditional routing | 🚀 Fast | Single |
| **Decision** | ⭐⭐⭐ | Classification + response | 🚀 Fast | Single |
| **Tool** | ⭐⭐⭐⭐ | Autonomous reasoning | 🚊 Slow | Single |
| **Multitask** | ⭐⭐⭐⭐ | Complex pipelines | 🚊 Slow | Single |
| **Q&A** | ⭐⭐⭐ | Document-based answers | ⚡ Medium | Single |
| **Memory** | ⭐⭐⭐ | Multi-turn dialogue | ⚡ Medium | Single |
| **Summarization** | ⭐⭐⭐ | Text condensation | ⚡ Medium | Multiple |

---

## 🎯 When to Use Which Chain

```
Simple task? → Traditional Chain
  ↓
Multiple independent tasks? → Parallel Chain
  ↓
Need to route conditionally? → Router Chain
  ↓
Need to classify and respond? → Decision Chain
  ↓
Multiple sequential steps? → Sequential Chain or Multitask Chain
  ↓
Need agent autonomy? → Tool Chain
  ↓
Context-based answers? → Q&A Chain
  ↓
Multi-turn dialogue? → Memory Chain
  ↓
Summarization needed? → Summarization Chain
```

---

## 📁 File Organization

```
langchain/
├── README.md                    ← Main documentation
├── QUICK_REFERENCE.md          ← This file
├── .env                         ← API keys (add your GROQ_API_KEY)
│
├── py_files/                    ← All Python code
│   ├── requirements.txt
│   ├── traditional.py           (⭐ Start here)
│   ├── sequential_chain.py
│   ├── parallel_chain.py
│   ├── router_chain.py
│   ├── decision_chain.py
│   ├── tool_chain.py
│   ├── multitask_chain.py
│   ├── qa_chain.py
│   ├── memory_chain.py
│   └── summarization_chain.py
│
└── results/                     ← All output files
    ├── traditional_result.txt
    ├── sequential_result.txt
    ├── parallel_result.txt
    ├── router_result.txt
    ├── decision_result.txt
    ├── tool_result.txt
    ├── multitask_result.txt
    ├── qa_result.txt
    ├── memory_result.txt
    └── summarization_result.txt
```

---

## ⚙️ Common Code Patterns

### 1. Basic Sequential (Traditional)
```python
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatGroq(model="openai/gpt-oss-120b")
prompt = PromptTemplate(template="...", input_variables=["var"])
parser = StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({"var": "value"})
```

### 2. Parallel Processing
```python
from langchain_core.runnables import RunnableParallel

chain = RunnableParallel(
    task1=prompt1 | model | parser,
    task2=prompt2 | model | parser,
    task3=prompt3 | model | parser,
)
result = chain.invoke({"input": "data"})
# result = {"task1": "...", "task2": "...", "task3": "..."}
```

### 3. Conditional Routing
```python
from langchain_core.runnables import RunnableLambda

def router(x):
    if "condition" in x["input"]:
        return chain1
    return chain2

chain = RunnableLambda(router)
```

### 4. Decision Branching
```python
from langchain_core.runnables import RunnableBranch, RunnablePassthrough

chain = (
    RunnablePassthrough.assign(decision=classifier)
    | RunnableBranch(
        (lambda x: x["decision"] == "A", chainA),
        (lambda x: x["decision"] == "B", chainB),
        fallback_chain,
    )
)
```

### 5. Tool-Based Agent
```python
from langchain_core.tools import tool
from langchain.agents import initialize_agent, AgentType

@tool
def my_tool(input: str) -> str:
    """Tool description"""
    return "result"

agent = initialize_agent(
    [my_tool],
    model,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
result = agent.invoke("query")
```

---

## 🔧 Setup Instructions

### 1. Install Python 3.9+
```bash
python --version  # Check if >= 3.9
```

### 2. Create Virtual Environment
```bash
python -m venv langchain_env
source langchain_env/bin/activate  # On Windows: langchain_env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r py_files/requirements.txt
```

### 4. Set Up Environment Variables
Create `.env` file in root directory:
```
GROQ_API_KEY=your_api_key_here
```

Get your API key from: https://console.groq.com/

### 5. Run a Chain
```bash
cd py_files
python sequential_chain.py
```

---

## 📊 Understanding Chain Output

Each result file contains three sections:

### Section 1: Chain Graph
```
+--------+
| Input  |
+--------+
    |
    v
+-------+
| Model |
+-------+
    |
    v
+--------+
| Output |
+--------+
```

### Section 2: Configuration
- Model name
- Prompt details
- Processing steps

### Section 3: Actual Output
The real LLM response to your input

---

## 🐛 Troubleshooting

### Problem: "Module not found"
```bash
# Solution: Install missing package
pip install langchain langchain-core langchain-groq python-dotenv
```

### Problem: "API key not found"
```bash
# Solution: Create .env file with your key
echo "GROQ_API_KEY=your_key_here" > .env
```

### Problem: "Rate limit exceeded"
```bash
# Solution: Add delay between requests
import time
time.sleep(2)  # Wait 2 seconds
result = chain.invoke(input_data)
```

### Problem: Long response times
```bash
# Solution: Use parallel chains instead of sequential
# Parallel chains are 2-3x faster for independent tasks
```

---

## 💡 Tips & Tricks

### 1. Pipe Operator (`|`)
The pipe operator chains operations:
```python
# Instead of:
result1 = prompt.invoke(data)
result2 = model.invoke(result1)
result3 = parser.invoke(result2)

# Write:
chain = prompt | model | parser
result3 = chain.invoke(data)
```

### 2. Visualize Chains
```python
chain.get_graph().print_ascii()  # ASCII visualization
```

### 3. Debug Individual Steps
```python
# Test each step separately
prompt_output = prompt.invoke({"var": "value"})
model_output = model.invoke(prompt_output)
final_output = parser.invoke(model_output)
```

### 4. Use Lambda for Transformation
```python
chain = (
    step1
    | (lambda x: {"key": x})  # Transform output
    | step2
)
```

### 5. Combine Chains
```python
combined = chain1 | chain2 | chain3
result = combined.invoke(data)
```

---

## 📚 Learning Path

**Beginner (Start Here)**
1. Read: `README.md` - Introduction section
2. Run: `traditional.py`
3. Run: `sequential_chain.py`
4. Understand: How prompts, models, and parsers work

**Intermediate**
5. Run: `parallel_chain.py`
6. Run: `router_chain.py`
7. Study: How conditional logic works
8. Run: `decision_chain.py`

**Advanced**
9. Run: `tool_chain.py`
10. Run: `multitask_chain.py`
11. Study: Complex multi-step workflows
12. Run: `qa_chain.py` and `memory_chain.py`

**Expert**
13. Modify existing chains
14. Create custom chains
15. Build production applications

---

## 🚀 Next Steps

### Build Your Own Chain
```python
# Start with template
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatGroq(model="openai/gpt-oss-120b")

# 1. Create prompt
my_prompt = PromptTemplate(
    template="You are helpful. {question}",
    input_variables=["question"]
)

# 2. Create chain
my_chain = my_prompt | model | StrOutputParser()

# 3. Test it
result = my_chain.invoke({"question": "What is AI?"})
print(result)

# 4. Save results
with open("my_result.txt", "w") as f:
    f.write(result)
```

### Combine Multiple Chains
```python
# Use parallel chains for performance
combined = RunnableParallel(
    summary=chain1,
    keywords=chain2,
    sentiment=chain3,
)

result = combined.invoke({"text": "input"})
```

---

## 📖 Documentation Links

- [LangChain Docs](https://python.langchain.com/)
- [Groq API](https://console.groq.com/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)

---

## 🎓 Real-World Applications

1. **Customer Support**: Memory Chain + Q&A Chain
2. **Content Generation**: Sequential Chain + Summarization
3. **Data Analysis**: Parallel Chain + Router Chain
4. **Research Assistant**: Q&A Chain + Memory Chain
5. **Sentiment Analysis**: Decision Chain + Multi-task responses
6. **Chatbots**: Memory Chain + Tool Chain
7. **Document Processing**: Summarization + Q&A Chains

---

## ⚡ Performance Tips

| Optimization | Benefit | Cost |
|-------------|---------|------|
| Use Parallel Chains | 3x faster | More API calls |
| Cache results | Instant repeat | Memory usage |
| Reduce context length | Faster, cheaper | Less context |
| Use smaller model | Cheaper, faster | Lower quality |
| Batch requests | Cost efficient | Higher latency |

---

## 🔐 Best Practices

✅ **DO**
- Always include error handling
- Test components separately
- Use type hints with Pydantic
- Monitor API usage
- Document your chains
- Version your prompts
- Use .env for secrets

❌ **DON'T**
- Hardcode API keys
- Use chains without testing
- Create overly long prompts
- Ignore rate limits
- Skip error handling
- Mix model types randomly
- Store sensitive data in code

---

**Written by Harshit**

*Happy Chaining! 🚀*
