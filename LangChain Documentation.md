### Tools :

Tools are specific functions that Agents can use to complete tasks
Ex: A Calculator tool , A Search Engine tool and A Calendar tool

### Agents :

- Agents help language models decide what actions to take when solving a problem.
- They choose the right tools at the right time without us telling them which tool to use
- Now you will have a doubt how does the Agent know what to do first and what to do second
- This is where the concept of reACT(Reasoning + Acting) comes in.It consists of Thought + Action + Observation

**Agent Control Flow**

1. **Prompt Initialisation**
   - An instruction to the LLM about its task
   - A description of available tools,including their names and usage details
     
2. **Agent Execution**
   - When the user provides a query to the agent the LLM interprets the query and generates a response
   - The LLM does not directly exceute the tools instead it suggests what tool to call and optionally provides arguments based on its reasoning.
     
4. **Tool Invocation**
   - The agents framework intercepts the LLM's output to check if it suggests a tool invocation
   - If a tool is suggested LangChain calls the tool in your python code passing in any arguments the LLM has proposed
     
5. **Tool Execution**
   - The tool runs in your Python environment with access to your systems resources (like the current time,file system,API's etc)
   - The tool returns its result to LangChain

6. **LLM Response :**
   - LangChain sends the tools output back to the LLM for further reasoning or generating a final response for the user
