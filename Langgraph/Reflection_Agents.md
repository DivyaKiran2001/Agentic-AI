### Reflection Agent Pattern :

A Reflection agent pattern is an AI system pattern that can look at its own outputs and think about them/make it better - 
just like how we look at ourselves in a mirror and self-reflect,make ourselves better

A basic reflection agent system typically consists of :
1. A generator agent
2. A reflector agent

**Types of Reflection agents in LangGraph**:

There are 3 types :

1. Basic Reflection Agents
2. Reflexion Agents
3. Language Agent Tree Search (LATS)

**Structured Outputs**:

- It is often useful to have a model return output that matches a specific schema that we define

**Example :**

**Input :** "Tell me a joke about cats"
**Output:**

{
  'setup' : 'Why was the cat sitting on the computer',
  'punchline' : 'Because it wanted to keep an eye on the mouse!'
}

**NOTE** : We have options to get outputs in formats such as - JSON,Dictionary,string and YAML

**1. Pydantic Models for Structured Outputs :**

   - Pydantic is a Python library that helps define data structures
   - Acts like a "blueprint" for data
   - Uses Python's type hints (like str,int) to enforce correct data types

**How it works in LangChain/LangGraph:**

1. Define a class with the fields you need (name,capital,language)
2. Add descriptions to explain what each field means
3. Use with _structued_output() to tell the LLM to follow your format

<pre>```python 
from pydantic import BaseModel,Field
from langchain_google_genai import ChatGoogleGenerativeAI

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

## With the mentioned Schema
class Country(BaseModel):
    """Information about a country"""
    name : str = Field(description="name of the country")
    language : str = Field(description="language of the country")
    capital : str = Field(description="Capital of the country")


structured_llm = llm.with_structured_output(Country)
structured_llm
structured_llm.invoke("Tell me about France")
```</pre> 


# Without rule of any predefined format (Schema)

<pre>```python 
from typing_extensions import Annotated,TypedDict
from typing import Optional

#TypedDict
class Joke(TypedDict):
    """Joke to tell user"""

    setup: Annotated[str,...,"The setup of the joke"]

    punchline: Annotated[str,...,"The punchline of the joke"]
    rating : Annotated[Optional[int],None,"How funny the joke is,from 1 to 10"]

structured_llm=llm.with_structured_output(Joke)
structured_llm.invoke("Tell me a joke about cats")
```</pre> 

