#basic.py

from typing import List,Sequence
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.graph import END,MessageGraph
from chains import generation_chain,reflection_chain

load_dotenv()

graph = MessageGraph()

REFLECT = "reflect"
GENERATE = "generate"

graph=MessageGraph()
def generate_node(state):
    return generation_chain.invoke({
        "messages":state
    }
    )

def reflect_node(messages):
    response=reflection_chain.invoke({
        "messages":messages
    })
    return [HumanMessage(content=response.content)]



graph.add_node(GENERATE,generate_node)
graph.add_node(REFLECT,reflect_node)

graph.set_entry_point(GENERATE)

def should_continue(state):
    if len(state)>4:
        return END
    return REFLECT

graph.add_conditional_edges(GENERATE,should_continue)
graph.add_edge(REFLECT,GENERATE)

app = graph.compile()

print(app.get_graph().draw_mermaid())
app.get_graph().print_ascii()

response=app.invoke(HumanMessage(content="AI agents taking over content creation"))
print(response)


##Output sample

# [
#   HumanMessage("AI agents taking over content creation"),
#   AIMessage("AI agents aren't stealing jobs..."),
#   HumanMessage("Great start! Consider hashtags..."),
#   AIMessage("AI agents aren't stealing jobs—they're creating new ones! #AI #ContentCreation 💡"),
#   HumanMessage("Try making it more emotionally engaging.")
# ]


--------------------------------------------------------------------------------------------------------

#chains.py

from langchain.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a twitter techie influencer assistant tasked with writing excellent twitter posts."
            "Generate the best twitter post possible for the user's request"
            "If the user provides critique, respond with a revised version of your previous attempts.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)


reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet. Generate critique and recommendations for the user's tweet."
            "Always provide detailed recommendations, including requests for length,virality, style etc."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro")

generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm

