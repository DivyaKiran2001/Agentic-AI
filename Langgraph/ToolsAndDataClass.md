# 🛠️ `@tool` and `ToolNode` in LangGraph

LangGraph and LangChain allow you to integrate **custom Python functions** as tools that an LLM can call. This is done using the `@tool` decorator and `ToolNode`.

---

## ✅ What is `@tool`?

`@tool` is a decorator used to convert a **regular Python function** into a tool that a language model can:
- **Recognize**
- **Call**
- **Use structured inputs/outputs**

### 🔹 Why use `@tool`?
- Automatically registers your function as a callable tool
- Makes input/output structured (using type hints)
- Helps LLMs choose and invoke tools correctly
- Allows integration with `bind_tools()` or tool_choice in LangGraph

---




## 📦 Simple Example

```python
from langchain_core.tools import tool

@tool
def add(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
llm_with_tools = llm.bind_tools(tools=[add])
response = llm_with_tools.invoke("Add 7 and 8")
```
### ToolNode

from langgraph.graph import ToolNode

tool_node = ToolNode(tools=add)

```python
from typing import TypedDict,Annotated
from langgraph.graph import add_messages,StateGraph,END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage,HumanMessage
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

load_dotenv()

class BasicChatBot(TypedDict):
    messages:Annotated[list,add_messages]

search_tool = TavilySearchResults(max_results=2)
tools=[search_tool]

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")
llm_with_tools = llm.bind_tools(tools=tools)

result = llm_with_tools.invoke("What is the time now")
# print(result)

def chatbot(state:BasicChatBot):
    return {
        "messages":[llm_with_tools.invoke(state["messages"])]
    }

def tools_router(state:BasicChatBot):
    last_message = state["messages"][-1]
    if(hasattr(last_message,"tool_calls") and len(last_message.tool_calls)>0):
        return "tool_node"
    else:
        return END

tool_node = ToolNode(tools=tools)

graph = StateGraph(BasicChatBot)
graph.add_node("chatbot",chatbot)
graph.add_node("tool_node",tool_node)
graph.set_entry_point("chatbot")
graph.add_conditional_edges("chatbot",tools_router)
graph.add_edge("tool_node","chatbot")

app=graph.compile()


while True:
    user_input=input("User :")
    if(user_input in ["exit","end"]):
        break
    else:
        result = app.invoke({
            "messages":[HumanMessage(content=user_input)]
        })
        print(result)

```

| Parameter                                       | Purpose                                                                                                        |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `@tool(response_format="content_and_artifact")` | Splits tool output into human-readable text (`content`) and machine-usable or downloadable object (`artifact`) |
| Helps with                                      | File generation, charts, links, structured outputs                                                             |
| Used in                                         | LangGraph or agents where tool output is multimodal                                                            |


response_format="content_and_artifact" tells LangGraph:

“When this tool is called, split the output into two parts:

content: the main response

artifact: any additional files, URLs, or structured data generated”

This format is helpful when:

You want text + structured outputs (e.g., JSON, chart data, links)

You want to show both the response content and an attached artifact (like a file or HTML chart)

**Example :**

```python
from langchain_core.tools import tool

@tool(response_format="content_and_artifact")
def summarize_report(text: str) -> dict:
    """Summarizes text and returns content plus a downloadable PDF."""
    summary = "This is the summary of the report."
    pdf_link = "https://example.com/generated_summary.pdf"
    return {
        "content": summary,
        "artifact": {"type": "file", "uri": pdf_link}
    }
```
**Output :**

{
  "content": "This is the summary of the report.",
  "artifact": {
    "type": "file",
    "uri": "https://example.com/generated_summary.pdf"
  }
}

### @dataclass :

In LangGraph, **@dataclass** is commonly used to define:

Structured state for the graph (the memory or context it passes between nodes)

Inputs and outputs of tools and nodes

Pydantic-compatible objects when working with LLMs or structured outputs

✅ @dataclass for defining LangGraph state

✅ Pydantic for defining tool input/output structure






