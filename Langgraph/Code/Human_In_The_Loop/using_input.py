from typing import TypedDict,Annotated
from langchain_core.messages import HumanMessage
from langgraph.graph import add_messages,StateGraph,END
from langchain_google_genai import ChatGoogleGenerativeAI
import tweepy

class State(TypedDict):
    messages : Annotated[list,add_messages]

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

GENERATE_POST = "generate_post"
GET_REVIEW_DECISION = "get_review_decision"
POST="post"
COLLECT_FEEDBACK="collect_feedback"

def generate_post(state:State):
    return {
        "messages":[llm.invoke(state["messages"])]
    }

def get_review_decision(state:State):
    post_content = state["messages"][-1].content

    print("\n Current Twitter Post:\n")
    print(post_content)
    print("\n")

    print("Answer the below question to continue....")

    decision = input("Post to Twitter? {yes/no}: ")

    if decision.lower() == "yes":
        return POST
    else:
        return COLLECT_FEEDBACK
    

def post(state:State):
    final_post = state["messages"][-1].content
    print("\n Final Twitter Post:\n")
    print(final_post)
    print("\n ✅ Post has been approved and is now live on twitter !!")


def collect_feedback(state:State):
    feedback = input("How can I improve this post??")
    return {
        "messages":[HumanMessage(content=feedback)]
    }

graph = StateGraph(State)

graph.add_node(GENERATE_POST,generate_post)
graph.add_node(GET_REVIEW_DECISION,get_review_decision)
graph.add_node(COLLECT_FEEDBACK,collect_feedback)
graph.add_node(POST,post)


graph.set_entry_point(GENERATE_POST)

graph.add_conditional_edges(GENERATE_POST,get_review_decision)
graph.add_edge(POST,END)
graph.add_edge(COLLECT_FEEDBACK,GENERATE_POST)

app=graph.compile()

response = app.invoke({
    "messages":[HumanMessage(content="Write me a twitter post on how Agent AI works in real use cases give me some scenarios using LangGraph")]
})

print(response)
 
