

### Drawback of using Reflection Agent System :

- Although iteratively making a post better is significantly better than just prompting ChatGPT ,
  the content generated is still not grounded in live data

- It could be hallucination or outdated content and we have no way of knowing

### Reflexion Agent System

The reflexion agent , similar to reflection agent , not only critiques it's own responses but also fact checks it with external data 
by making API calls(Internet Search)

- In the reflexion agent pattern, we had to rely on the training data of LLM's but in this case.we're not limited to that

=> The main component of Reflexion agent system is the "actor"

=> The "actor" is the main agent that drives everything - it reflects on its responses and re-executes

=> It can do this with or without tools to improve based on self-critique that is grounded in external data

=> It's main sub-components include :

1. Tools/tool execution
2. **Initial responder :** Generate an initial response and self reflection
3. **Revisor :** re-respond and reflect based on previous reflections

**Episodic memory**:

- In the context of Reflexion agents,episodic memory refers to an agents ability to recall specific past interactions,events or experiences rather
- than just generalized knowledge

- - This is crucial for making agents feel more context aware,personalized and human-like over time

**LLM Response Parser System**:

The system converts unstructured LLM outputs into well defined Python objects through a series of structured parsing steps,ensurong data validation and consistent formatting

**What are the key components?**:

1. **Chat Prompt Template**
2. **Function Calling with Pydantic Schema**
   
   **Function Calling** :
     Similar to how we make tools available to the LLM,we can also send a achema to the LLM and force it to structure it's JSON output according to the schema
   **Pydantic**:
   - A Python library that defines data structures using classes
   - Provides automatic validation of JSON data against these class definitions
3. **Pydantic Parser**

   - Takes the JSON output from the LLM's function call
   - Validates it against the defined Pydantic schema (class definition)
   - Creates instances of Pydantic classes with the validated data
   - If the LLMs output does not match with the defined schema,it will throw an error
