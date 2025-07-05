### Agents and Tools :

1. Agents:
   - Agents are problem solvers of the AI world.Agents are capable of thinking on their own

2. Tools :
   - Tools are specific functions that Agents can use to complete tasks.

**Re-Act Agent Pattern**:

- It stands for Reasoning + Acting
  
  **Think** : LLM first thinks about the user prompt/problem
  
  **Action** : LLM decides if it can answer by itself or if it should use a tool
  
  **Action Input** : LLM provides the input argument for the tool
  
  **Observe** : LLM observe the result of the tool and return the output to the **Think** and the process repeats

  **Final Answer**: After all the aobe steps we have the final answer
