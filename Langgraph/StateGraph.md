### State :

- State in LangGraph is a way to maintain and track information as an AI system processes data
- Think of it as the system's memory, allowing it to remember and update information as it moves through different stages of a workflow or graph
  
**1. Manual State Transformation** :

In manual state transformation, you explicitly write functions that take the current state as input and return a new modified state. 
You are responsible for handling what part of the state gets read, updated, or returned.

**2. Declarative Annotated State Transformation**:

In declarative annotated state transformation, you use function annotations and decorators provided by LangGraph to automatically 
infer which parts of the state are needed and updated. LangGraph takes care of state extraction and merging.

You declare what parts of state a node:

needs (function parameters)

returns (function return values)
