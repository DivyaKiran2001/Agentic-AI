import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash",api_key=api_key)

## Invoking
# res=llm.invoke("Explain the main concepts of data engineering in azure in one line each")
# print(res)

template = "Explain the concept of {topic} in simple terms."

## String Prompt Template
# prompt_template=PromptTemplate.from_template("Do you know when was {person} born")
# prompt=prompt_template.invoke({"person":"Mahesh Babu"})
# final=llm.invoke(prompt)
# print(final)

## Chat Prompt Template
# prompt_template1=ChatPromptTemplate.from_template(template)
# prompt1=prompt_template1.invoke({
#     "topic":"Google Agent Development Kit(ADK)"
# })

# res1=llm.invoke(prompt1)
# print(res1.content)

## Using Chat Prompt Template with from_messages
messages = [
    ("system","Assume you are Content Writer that writes about {type} posts"),
    ("human","Help me to write a post on {topic}")
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({
    "type":"Linkedin",
    "topic" : "GCP Gen AI Services"
})
res=llm.invoke(prompt)
print(res)



