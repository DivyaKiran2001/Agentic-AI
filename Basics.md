### Prompt Templates :

- Prompt templates help to translate user input and parameters into instructions for a language model. 
- Prompt Templates take as input a dictionary, where each key represents a variable in the prompt
template to fill in.

https://python.langchain.com/docs/concepts/prompt_templates/

1. **String Prompt Templates :**

These prompt templates are used to format a single string, and generally are used for simpler inputs.
For example, a common way to construct and use a PromptTemplate is as follows:

**Example :**

from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template("Tell me a joke about {topic}")

prompt_template.invoke({"topic": "cats"})

2. **ChatPromptTemplates :**

These prompt templates are used to format a list of messages. These "templates" consist of a list of templates themselves. 
For example, a common way to construct and use a ChatPromptTemplate is as follows

**Example:**

from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate([
    ("system", "You are a helpful assistant"),
    ("user", "Tell me a joke about {topic}")
])

prompt_template.invoke({"topic": "cats"})


