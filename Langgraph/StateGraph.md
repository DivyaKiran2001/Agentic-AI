### State :

- State in LangGraph is a way to maintain and track information as an AI system processes data
- Think of it as the system's memory, allowing it to remember and update information as it moves through different stages of a workflow or graph
  
**1. Manual State Transformation** :

In manual state transformation, you explicitly write functions that take the current state as input and return a new modified state. 
You are responsible for handling what part of the state gets read, updated, or returned.\

**Example :**

def step(state: dict) -> dict:

    user_input = state["input"]  # read from state
    
    # update history manually
    
    state["history"] = state.get("history", []) + [f"User: {user_input}"]
    
    return state  # return full updated state


**2. Declarative Annotated State Transformation**:

In declarative annotated state transformation, you use function annotations and decorators provided by LangGraph to automatically 
infer which parts of the state are needed and updated. LangGraph takes care of state extraction and merging.

You declare what parts of state a node:

needs (function parameters)

returns (function return values)


**Example :**

from typing import TypedDict,List,Annotated
from langgraph.graph import END,StateGraph
import operator

class SimpleState(TypedDict):
    count:int
    sum:Annotated[int,operator.add]
    history:Annotated[List[int],operator.concat]

def increment(state : SimpleState) -> SimpleState:
    new_count=state["count"]+1
    # new_sum = state["sum"] + new_count
    # print(f"Incrementing: count={new_count}, sum={new_sum}")
    return {
        "count":new_count,
        "sum":new_count,
        "history":[new_count]
    }

def should_continue(state):
    if(state["count"]<5):
        return "continue"
    else:
        return "stop"
    
graph=StateGraph(SimpleState)
graph.add_node("increment",increment)
graph.set_entry_point("increment")
graph.add_conditional_edges("increment",should_continue,{
    "continue":"increment",
    "stop":END
})

app=graph.compile()
state = {
    "count":0,
    "sum":0,
    "history":[]
}
res=app.invoke(state)
print(res)

