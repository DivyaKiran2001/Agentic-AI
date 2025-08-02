### Message Graph

It is a class that Langgraph provides that we can use to orchestrate the flow of messages between different nodes

**In Simple Terms** : MessageGraph maintains a list of messages and decides the flow of messages between nodes

- Every node in MessageGraph receives the full list of previous messages as input
- Each node can append new messages to the list and return it
- The updated message list is then passed to the next node

Example Use cases : Simple routing decisions,simple chatbot conversation flow

**NOTE** : If the app requires complex state management, we have StateGraph 

**add_messages :**

In LangGraph, add_messages is a helper function that adds new messages to the chat history (part of the state).

It's often used when you're working with chat-based models (like OpenAI’s gpt-4, Claude, Gemini, etc.) in LangGraph.

**Example :**
<pre> ```python
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph

class State(TypedDict):
    messages: Annotated[list, add_messages]

builder = StateGraph(State)
builder.add_node("chatbot", lambda state: {"messages": [("assistant", "Hello")]})
builder.set_entry_point("chatbot")
builder.set_finish_point("chatbot")
graph = builder.compile()
graph.invoke({})
# {'messages': [AIMessage(content='Hello', id=...)]}
``` </pre>

