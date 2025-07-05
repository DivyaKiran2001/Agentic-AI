# Install the below packages below before running the code and set Google gemini api key and tavily api key 
#pip install langchain langchain_community langchain-google-genai python-dotnev





from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from datetime import date
from langchain.agents import initialize_agent
from langchain_community.tools import TavilySearchResults,tool

load_dotenv()
llm= ChatGoogleGenerativeAI(model="gemini-1.5-pro")
search_tools=TavilySearchResults(search_depth="basic")
# res=llm.invoke("How is the weather today in hyderabad will it rain today evening")
# print(res.content)

@tool
def get_current_date(format :str="%Y-%m-%d"):
    """ Returns current date"""
    return date.today()

tools=[search_tools,get_current_date]

agent = initialize_agent(tools=tools,llm=llm,agent="zero-shot-react-description",verbose=True)
agent.invoke("When was Mahesh babu was born and what is the age of him at present?")
