import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from dotenv import load_dotenv
from langchain.schema.output_parser import StrOutputParser

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash",api_key=api_key)
messages = [
    ("system","Assume you are Content Writer that writes about {type} posts"),
    ("human","Help me to write a post on {topic}")
]

prompt_template = ChatPromptTemplate.from_messages(messages)

## LCEL
chain = prompt_template | llm | StrOutputParser()

res = chain.invoke({"type":"Instagram","topic":"Movies"})
print(res)
