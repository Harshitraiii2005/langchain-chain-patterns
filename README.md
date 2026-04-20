# LangChain Chains: A Comprehensive Guide

**Written by Harshit**

---

## 📚 Table of Contents

1. [Introduction](#introduction)
2. [What are Chains?](#what-are-chains)
3. [Why Chains Matter in LangChain](#why-chains-matter)
4. [Types of Chains](#types-of-chains)
5. [Chain Implementations](#chain-implementations)
6. [How to Run](#how-to-run)
7. [Results Interpretation](#results-interpretation)
8. [Best Practices](#best-practices)

---

## Introduction

This repository contains comprehensive implementations of various **LangChain Chain patterns** with practical examples. LangChain is a powerful framework that simplifies the development of applications powered by large language models (LLMs). Chains are one of the core components that enable complex, multi-step interactions with LLMs.

This project demonstrates 10 different chain types, each solving real-world problems with increasing complexity.

---

## What are Chains?

In LangChain, a **Chain** is a sequence of calls to LLMs or other tools, executed in a specific order. Chains allow you to:

- **Combine multiple prompts** to break complex tasks into smaller steps
- **Use output from one step** as input to the next
- **Process data through different models** in sequence
- **Create dynamic workflows** that adapt based on intermediate results
- **Maintain context** throughout multi-turn interactions

### Basic Concept

```
Input → Prompt Template → LLM → Parser → Output → Next Chain Step → Final Output
```

---

## Why Chains Matter in LangChain

### 1. **Breaking Down Complex Problems**
Instead of writing one massive prompt for a complex task, chains break it into manageable steps. Each step handles a specific aspect, making the solution more robust and debuggable.

### 2. **Composability**
Chains are composable - you can combine simpler chains to create more complex ones. This follows the Unix philosophy: "Do one thing and do it well."

### 3. **Reusability**
Once you define a chain, you can reuse it in different applications. The modular structure promotes clean code and consistency.

### 4. **Better Error Handling**
With chains, failures are isolated to specific steps, making it easier to identify and fix issues.

### 5. **Performance Optimization**
Chains can be parallelized when steps don't depend on each other, significantly improving execution time for large tasks.

### 6. **Memory and Context Management**
Chains help maintain context across multiple interactions, enabling more natural and coherent conversations.

### 7. **Type Safety and Validation**
Using structured outputs (Pydantic models) in chains ensures data integrity throughout the pipeline.

---

## Types of Chains

### 1. **Sequential Chain** (Simple Sequential Execution)
- **Purpose:** Execute prompts one after another, with each step receiving output from the previous
- **Use Case:** Writing → Reviewing → Grading workflow
- **File:** `sequential_chain.py`
- **Key Feature:** Linear pipeline with clear data flow

### 2. **Parallel Chain** (Concurrent Execution)
- **Purpose:** Execute multiple prompts simultaneously on the same input
- **Use Case:** Generate report + MCQs + explanation for a topic in parallel
- **File:** `parallel_chain.py`
- **Key Feature:** `RunnableParallel` for concurrent processing
- **Benefit:** Significantly faster execution when tasks are independent

### 3. **Router Chain** (Conditional Routing)
- **Purpose:** Route input to different chains based on conditions
- **Use Case:** Route MCQ requests to MCQ generator, others to explainer
- **File:** `router_chain.py`
- **Key Feature:** `RunnableLambda` for custom routing logic
- **Benefit:** Smart task distribution based on input characteristics

### 4. **Decision Chain** (Branching Logic)
- **Purpose:** Make decisions based on intermediate outputs and branch accordingly
- **Use Case:** Classify sentiment and respond differently based on classification
- **File:** `decision_chain.py`
- **Key Feature:** `RunnableBranch` for structured decision-making
- **Benefit:** Type-safe branching with Pydantic models

### 5. **Tool Chain** (Agent-Based Execution)
- **Purpose:** Use an agent to choose and execute tools dynamically
- **Use Case:** AI agent that can perform calculations, search, and reasoning
- **File:** `tool_chain.py`
- **Key Feature:** `AgentType.ZERO_SHOT_REACT_DESCRIPTION`
- **Benefit:** Autonomous agent behavior with tool selection

### 6. **Traditional Chain** (LLM + Prompt + Parser)
- **Purpose:** Basic pipe chain combining prompt, model, and parser
- **Use Case:** Simple text generation and processing
- **File:** `traditional.py`
- **Key Feature:** Foundational pattern used in many chains
- **Benefit:** Simple and elegant for straightforward tasks

### 7. **Multitask Chain** (Sequential Complex Processing)
- **Purpose:** Execute multiple chained tasks where each step transforms the output
- **Use Case:** Write paragraph → Review → Evaluate workflow
- **File:** `multitask_chain.py`
- **Key Feature:** Lambda functions for dynamic transformation
- **Benefit:** Complex sequential processing with data transformation

### 8. **Question Answering Chain** (Context-Based QA)
- **Purpose:** Answer questions based on provided context/documents
- **Use Case:** Document QA systems, knowledge base search
- **File:** `qa_chain.py`
- **Key Feature:** Context-aware prompt templates
- **Benefit:** Build RAG (Retrieval-Augmented Generation) systems

### 9. **Memory/Conversation Chain** (Context Preservation)
- **Purpose:** Maintain conversation history and context across turns
- **Use Case:** Chatbots and multi-turn dialogue systems
- **File:** `memory_chain.py`
- **Key Feature:** Manual memory management with history formatting
- **Benefit:** Stateful interactions with context awareness

### 10. **Summarization Chain** (Text Condensation)
- **Purpose:** Generate abstracts, detailed summaries, and key points
- **Use Case:** Document processing, content condensation
- **File:** `summarization_chain.py`
- **Key Feature:** Multiple levels of summarization
- **Benefit:** Flexible text processing at different granularities

---

## Chain Implementations

### Project Structure

```
langchain/
├── py_files/                      # All Python implementation files
│   ├── requirements.txt           # Project dependencies
│   ├── sequential_chain.py        # Sequential chain implementation
│   ├── parallel_chain.py          # Parallel chain implementation
│   ├── router_chain.py            # Router chain implementation
│   ├── decision_chain.py          # Decision chain implementation
│   ├── tool_chain.py              # Tool/Agent chain implementation
│   ├── traditional.py             # Traditional LLM chain
│   ├── multitask_chain.py         # Multitask chain implementation
│   ├── qa_chain.py                # Question answering chain
│   ├── memory_chain.py            # Memory/Conversation chain
│   └── summarization_chain.py     # Summarization chain
│
└── results/                       # All execution results
    ├── sequential_result.txt      # Sequential chain output
    ├── parallel_result.txt        # Parallel chain output
    ├── router_result.txt          # Router chain output
    ├── decision_result.txt        # Decision chain output
    ├── traditional_result.txt     # Traditional chain output
    ├── multitask_result.txt       # Multitask chain output
    ├── qa_result.txt              # Q&A chain output
    ├── memory_result.txt          # Memory chain output
    └── summarization_result.txt   # Summarization chain output
```

---

## Detailed Code Explanations

### 1. Sequential Chain (`sequential_chain.py`)

**What it does:**
Creates a simple pipe chain where each component processes the input sequentially.

**Key Components:**
- `PromptTemplate`: Formats input with placeholders
- `ChatGroq`: LLM that processes the prompt
- `StrOutputParser`: Converts LLM output to string

**Code Pattern:**
```python
chains = prompt1 | model | parser
result = chains.invoke({"text": "topic"})
```

**When to use:**
- Simple prompting tasks
- When you need a straightforward input → output flow
- Building blocks for more complex chains

---

### 2. Parallel Chain (`parallel_chain.py`)

**What it does:**
Executes multiple prompts in parallel on the same input, collecting all results.

**Key Components:**
- `RunnableParallel`: Orchestrates parallel execution
- Multiple `PromptTemplate` instances for different tasks
- Named outputs: `explanation`, `report`, `mcq`

**Code Pattern:**
```python
chain = RunnableParallel(
    explanation=prompt3 | model | parser,
    report=prompt1 | model | parser,
    mcq=prompt2 | model | parser
)
result = chain.invoke({"topic": "Machine Learning"})
```

**When to use:**
- Generate multiple perspectives on the same topic
- Improve efficiency by parallelizing independent tasks
- When you need different outputs from one input

**Performance Benefit:** 3x faster than sequential for 3 independent tasks

---

### 3. Router Chain (`router_chain.py`)

**What it does:**
Routes input to different processing chains based on conditional logic.

**Key Components:**
- `RunnableLambda`: Custom function for routing decision
- Conditional logic checking input content
- Different prompts for different routes

**Code Pattern:**
```python
def router(x):
    if "mcq" in x["topic"].lower():
        return prompt_mcq | model | parser
    return prompt_explain | model | parser

chain = RunnableLambda(router)
```

**When to use:**
- Intent classification and routing
- Different handling based on input type
- Smart workflow selection
- API endpoints that need intelligent routing

---

### 4. Decision Chain (`decision_chain.py`)

**What it does:**
Makes structured decisions using Pydantic models and branches execution accordingly.

**Key Components:**
- `PydanticOutputParser`: Type-safe output parsing
- `RunnableBranch`: Structured branching logic
- Classification model (detects sentiment)
- Three response templates (positive, negative, neutral)

**Code Pattern:**
```python
chain = (
    RunnablePassthrough.assign(sentiment=classifier_chain)
    | RunnableBranch(
        (lambda x: x["sentiment"] == "positive", prompt2 | model | parser),
        (lambda x: x["sentiment"] == "negative", prompt3 | model | parser),
        (lambda x: x["sentiment"] == "neutral", prompt4 | model | parser),
    )
)
```

**When to use:**
- Sentiment analysis with different responses
- Classification-driven workflows
- Type-safe decision making
- When you need structured output

---

### 5. Tool Chain (`tool_chain.py`)

**What it does:**
Uses an LLM agent with tools to solve problems autonomously.

**Key Components:**
- `@tool` decorator for function definition
- `AgentType.ZERO_SHOT_REACT_DESCRIPTION`: Reasoning agent
- `initialize_agent`: Sets up the agent
- Tool list: Available functions the agent can call

**Code Pattern:**
```python
@tool
def multiply(a: int, b: int) -> int:
    return a * b

tools = [multiply]
agent = initialize_agent(tools, model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
result = agent.invoke("What is 5 multiplied by 6?")
```

**When to use:**
- Complex reasoning tasks requiring tool usage
- Autonomous agent behavior
- Multi-step reasoning with external functions
- When the LLM needs to decide which tools to use

---

### 6. Traditional Chain (`traditional.py`)

**What it does:**
Basic chain combining prompt template, LLM, and output parser.

**Key Components:**
- Simple prompt template
- Model invocation
- Output parsing

**Code Pattern:**
```python
prompt1 = PromptTemplate(template="...", input_variables=["text"])
result = model.invoke(template)
final_result = parser.invoke(result)
```

**When to use:**
- Quick prototyping
- Simple text generation
- Foundation for building complex chains
- Learning LangChain basics

---

### 7. Multitask Chain (`multitask_chain.py`)

**What it does:**
Executes multiple chained tasks with data transformation between steps.

**Key Components:**
- Sequential prompts (Writer → Reviewer → Evaluator)
- Lambda functions for data transformation
- Multiple LLM calls in sequence

**Code Pattern:**
```python
chains = (
    prompt1 | model | parser
    | (lambda x: {"paragraph": x})
    | prompt2 | model | parser
    | (lambda x: {"paragraph": x})
    | prompt3 | model | parser
)
```

**When to use:**
- Multi-stage processing pipelines
- When each stage requires different prompts
- Iterative refinement workflows (write → review → grade)
- Complex task decomposition

---

### 8. Question Answering Chain (`qa_chain.py`)

**What it does:**
Answers questions based on provided context/documents.

**Key Components:**
- Context-aware prompt template
- Multiple test questions
- Context variable in prompt

**Code Pattern:**
```python
qa_prompt = PromptTemplate(
    template="Answer based on context: {context}\nQuestion: {question}",
    input_variables=["context", "question"]
)
result = qa_chain.invoke({"context": context, "question": question})
```

**When to use:**
- Document QA systems
- Building RAG (Retrieval-Augmented Generation) systems
- Knowledge base queries
- Customer support chatbots

**Real-world Application:** Combine with vector databases for retrieving relevant context automatically

---

### 9. Memory/Conversation Chain (`memory_chain.py`)

**What it does:**
Maintains conversation history across multiple turns for stateful interactions.

**Key Components:**
- Conversation history tracking
- History formatting function
- Dynamic prompt that includes history

**Code Pattern:**
```python
def format_history():
    history_text = ""
    for i, msg in enumerate(conversation_history):
        if i % 2 == 0:
            history_text += f"User: {msg}\n"
        else:
            history_text += f"Assistant: {msg}\n"
    return history_text

prompt = PromptTemplate(
    template="History:\n{history}\n\nUser: {input}",
    input_variables=["history", "input"]
)
```

**When to use:**
- Multi-turn chatbots
- Maintaining context in conversations
- Dialogue systems
- Customer support where context matters

---

### 10. Summarization Chain (`summarization_chain.py`)

**What it does:**
Generates summaries at different levels of detail from a document.

**Key Components:**
- Multiple prompt templates for different summary types
- Abstract summary (2-3 sentences)
- Detailed summary (5-7 sentences)
- Key points extraction

**Code Pattern:**
```python
abstract_chain = abstract_summary_prompt | model | parser
detailed_chain = detailed_summary_prompt | model | parser
bullet_chain = bullet_point_prompt | model | parser

# Run all chains on the same document
abstract_result = abstract_chain.invoke({"text": document})
detailed_result = detailed_chain.invoke({"text": document})
```

**When to use:**
- Document processing systems
- Content condensation
- Generating multiple summary types
- News article summarization
- Research paper abstracts

---

## How to Run

### Prerequisites

```bash
# Install dependencies
pip install -r py_files/requirements.txt
```

### Running Individual Chains

```bash
# Navigate to py_files directory
cd py_files

# Run any chain
python sequential_chain.py      # Sequential chain
python parallel_chain.py        # Parallel chain
python router_chain.py          # Router chain
python decision_chain.py        # Decision chain
python tool_chain.py            # Tool chain
python traditional.py           # Traditional chain
python multitask_chain.py       # Multitask chain
python qa_chain.py              # Q&A chain
python memory_chain.py          # Memory chain
python summarization_chain.py   # Summarization chain
```

### Viewing Results

All results are saved to the `results/` folder:

```bash
# View results
cd ../results
cat sequential_result.txt
cat parallel_result.txt
# ... and so on
```

---

## Results Interpretation

Each result file contains:

1. **Chain Graph**: ASCII visualization of how data flows through the chain
2. **Output**: The actual result from the LLM
3. **Chain Architecture**: Shows the sequence of transformations

### Example Result Structure

```
===== [CHAIN_TYPE] CHAIN GRAPH =====
+-------------+       
| PromptInput |       
+-------------+       
       *              
+----------+         
| ChatGroq |         
+----------+         
       *              
+-----------+        
| Parser    |        
+-----------+        

===== RESULTS =====
[Actual LLM Output]
```

---

## Best Practices

### 1. **Start Simple, Build Complex**
Begin with traditional chains and gradually add complexity:
- Traditional → Sequential → Parallel → Router → Advanced

### 2. **Use Type Hints**
Use Pydantic models for structured outputs:
```python
from pydantic import BaseModel

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative", "neutral"]
```

### 3. **Error Handling**
Implement error handling in production:
```python
try:
    result = chain.invoke({"input": data})
except Exception as e:
    logger.error(f"Chain execution failed: {e}")
```

### 4. **Optimize Parallel Chains**
Use parallel chains when:
- Steps don't depend on each other's output
- Individual steps take significant time
- You can afford additional LLM API calls

### 5. **Test Components Independently**
Test each prompt and chain component separately before combining:
```python
# Test prompt alone
test_prompt = prompt.invoke({"input": "test"})

# Test model response
test_model = model.invoke(test_prompt)

# Then combine
chain = prompt | model | parser
```

### 6. **Monitor Token Usage**
Track API usage for cost management:
- Parallel chains use more tokens
- Consider batch processing for large datasets

### 7. **Use Structured Output**
Always parse outputs into structured formats:
```python
parser = PydanticOutputParser(pydantic_object=MyModel)
```

### 8. **Cache Results**
For repeated queries, implement caching:
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def cached_chain(query):
    return chain.invoke({"query": query})
```

### 9. **Version Your Prompts**
Keep track of prompt versions:
```
prompts/
├── v1_basic_prompt.txt
├── v2_improved_prompt.txt
└── v3_production_prompt.txt
```

### 10. **Document Your Chains**
Always include docstrings and comments explaining:
- Purpose of the chain
- Input requirements
- Expected output format
- Use cases and limitations

---

## Chain Selection Guide

**Need to...**

| Goal | Use This Chain | Example |
|------|---|---|
| Process input through multiple steps sequentially | Sequential | Write → Review → Finalize |
| Do independent tasks in parallel | Parallel | Get report + summary + MCQs simultaneously |
| Route based on conditions | Router | MCQ request → MCQ handler; Other → Explainer |
| Make decisions with branching | Decision | Classify sentiment → respond appropriately |
| Use tools autonomously | Tool/Agent | Let AI decide which calculator to use |
| Simple generate text | Traditional | Basic prompting |
| Multiple complex steps | Multitask | Writer → Reviewer → Evaluator |
| Answer questions from context | Q&A | Document Q&A system |
| Keep conversation context | Memory | Multi-turn chatbot |
| Create summaries | Summarization | Different summary levels |

---

## Advanced Topics

### 1. Streaming Responses
```python
for chunk in chain.stream({"input": "data"}):
    print(chunk, end="", flush=True)
```

### 2. Custom Runnable Classes
```python
class MyRunnable(Runnable):
    def invoke(self, input):
        # Custom logic
        return output
```

### 3. Async Execution
```python
result = await chain.ainvoke({"input": "data"})
```

### 4. Debugging Chains
```python
chain.get_graph().print_ascii()
chain.get_graph().draw_ascii()
```

---

## Troubleshooting

### Issue: "Module not found" error
**Solution:** Install missing dependencies
```bash
pip install -r requirements.txt
```

### Issue: API rate limiting
**Solution:** Add delays between requests
```python
import time
time.sleep(2)  # Wait 2 seconds
```

### Issue: Chain timeout
**Solution:** Increase timeout or optimize chain complexity
```python
result = chain.invoke(
    {"input": "data"},
    timeout=60  # 60 seconds
)
```

### Issue: Memory overflow with long conversations
**Solution:** Implement conversation history trimming
```python
if len(history) > 20:
    history = history[-10:]  # Keep last 10 messages
```

---

## Dependencies

- `langchain`: Core LangChain framework
- `langchain-core`: Core abstractions
- `langchain-groq`: Groq LLM integration
- `python-dotenv`: Environment variable management
- `pydantic`: Data validation using Python type annotations

---

## Environment Setup

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## Contributing

Feel free to:
- Add new chain types
- Improve existing implementations
- Add more examples
- Fix bugs
- Improve documentation

---

## License

This project is open source and available for educational and commercial use.

---

## Conclusion

Chains are the backbone of LangChain applications. By mastering these 10 chain patterns, you can build sophisticated LLM-powered applications ranging from simple text generation to complex multi-stage AI systems.

**Key Takeaways:**
1. Chains compose simple operations into complex workflows
2. Different chain types solve different problems
3. Choose the right chain for your use case
4. Always start simple and build up complexity
5. Test components independently before combining
6. Monitor performance and token usage

Happy chaining! 🚀

---

**Written by Harshit**

*Last Updated: April 21, 2026*
