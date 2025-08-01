from langgraph.graph import StateGraph,START,END,add_messages
from langgraph.types import Command,interrupt
from typing import TypedDict,Annotated,List
from langgraph.checkpoint.memory import MemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
import uuid
from dotenv import load_dotenv
import tweepy
import os
import certifi
import ssl

load_dotenv()
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

class State(TypedDict):
    twitter_topic : str
    generated_post : Annotated[List[str],add_messages]
    human_feedback : Annotated[List[str],add_messages]

def model(state:State):
     """ Here, we're using the LLM to generate a Twitter post with human feedback incorporated """
     print("[model] Generating Content")

     twitter_topic = state["twitter_topic"]
     feedback = state["human_feedback"] if "human_feedback" in state else ["No Feedback yet"]

     # Here, we define the prompt 

     prompt = f"""

            Twitter Topic: {twitter_topic}
            Human Feedback: {feedback[-1] if feedback else "No feedback yet"}

            Generate a structured and well-written Twitter post based on the given topic.

        Consider previous human feedback to refine the reponse. 
    """
     
     response = llm.invoke([
        SystemMessage(content="You are an expert Twitter content writer"), 
        HumanMessage(content=prompt)

      ])
     
     geneated_twitter_post = response.content

     print(f"[model_node] Generated post:\n{geneated_twitter_post}\n")

     return {
       "generated_post": [AIMessage(content=geneated_twitter_post)] , 
       "human_feedback": feedback
    }


def human_node(state:State):
    """Human Intervention node - loops back to model unless input is done"""

    print("\n [human_node] awaiting human feedback...")

    generated_post = state["generated_post"]

    user_feedback = interrupt(
        {
            "generated_post": generated_post, 
            "message": "Provide feedback or type 'done' to finish"
        }
    )

    print(f"[human_node] Received human feedback: {user_feedback}")

    # If user types "done", transition to END node
    if user_feedback.lower() == "done":
        return Command(update={"human_feedback":state["human_feedback"]+["Finalised"]},goto="end_node")
    
    # Otherwise, update feedback and return to model for re-generation
    return Command(update={"human_feedback": state["human_feedback"] + [user_feedback]}, goto="model")

def end_node(state:State):
    """ Final node """
    print("\n[end_node] Process finished")
    final_post = state["generated_post"][-1].content
    print("Final Generated Post:", state["generated_post"][-1])
    print("Final Human Feedback", state["human_feedback"])
    try:
        auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
        api = tweepy.API(auth)


        api.update_status(status=final_post)
        print("✅ Tweet successfully posted to Twitter!")
    except Exception as e:
        print(f"❌ Failed to post tweet: {e}")
    
    return {"generated_post": state["generated_post"], "human_feedback": state["human_feedback"]}

graph = StateGraph(State)

graph.add_node("model",model)
graph.add_node("human_node",human_node)
graph.add_node("end_node",end_node)

graph.set_entry_point("model")

graph.add_edge(START,"model")
graph.add_edge("model","human_node")

graph.set_finish_point("end_node")

checkpointer = MemorySaver()
app=graph.compile(checkpointer=checkpointer)

thread_config = {"configurable": {
    "thread_id": uuid.uuid4()
}}

twitter_topic = input("Enter the Twitter topic: ")  
initial_state = {
    "twitter_topic": twitter_topic, 
    "generated_post": [], 
    "human_feedback": []
}


for chunk in app.stream(initial_state, config=thread_config):
    for node_id, value in chunk.items():
        #  If we reach an interrupt, continuously ask for human feedback

        if(node_id == "__interrupt__"):
            while True: 
                user_feedback = input("Provide feedback (or type 'done' when finished): ")

                # Resume the graph execution with the user's feedback
                app.invoke(Command(resume=user_feedback), config=thread_config)

                # Exit loop if user says done
                if user_feedback.lower() == "done":
                    break
