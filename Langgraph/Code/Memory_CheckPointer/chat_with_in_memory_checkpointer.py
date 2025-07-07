from typing import TypedDict,Annotated
from langgraph.graph import add_messages,StateGraph,END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage,HumanMessage
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

memory = MemorySaver()

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

class BasicChatState(TypedDict):
    messages:Annotated[list,add_messages]

def chatbot(state:BasicChatState):
    return {
        "messages":[llm.invoke(state["messages"])]
    }

graph=StateGraph(BasicChatState)
graph.add_node("chatbot",chatbot)
graph.set_entry_point("chatbot")
graph.add_edge("chatbot",END)

app=graph.compile(checkpointer=memory)

config = {"configurable":{
    "thread_id":1
}}

response1=app.invoke({
    "messages":HumanMessage(content="Hi, I am Divya")
},config=config)

response2=app.invoke({
    "messages":HumanMessage(content="What's my name?")
},config=config)

print(response1)
print("\n")
print(response2)
