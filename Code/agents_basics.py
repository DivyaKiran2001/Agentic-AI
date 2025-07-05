import os
from dotenv import load_dotenv
from datetime import datetime
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import tool,initialize_agent,AgentType


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") 
print(api_key)



@tool
def get_current_time() -> str:
    """Returns the current system time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

tools=[get_current_time]

llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash",google_api_key=api_key,
                           temperature=0)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

response = agent.run("Hi,Can you tell what time is right now ?")
print(response)
