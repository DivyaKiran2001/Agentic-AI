import json
from typing import List,Dict,Any
from langchain_core.messages import AIMessage,BaseMessage,ToolMessage,HumanMessage
from langchain_community.tools import TavilySearchResults

#create the Tavily search tool
tavily_tool=TavilySearchResults(max_results=5)

# fUNCTION to execute search queries from AnswerQuestion tool calls

def execute_tools(state:List[BaseMessage]) -> List[BaseMessage]:

    # Extract tool calls from the AI Message

    last_ai_message:AIMessage = state[-1]

    if not hasattr(last_ai_message,"tool_calls") or not last_ai_message.tool_calls:
        return
    
    # Process the AnswerQuestion or ReviseAnswer tool calls to extract search queries

    tool_messages = []

    for tool_call in last_ai_message.tool_calls:
        if tool_call["name"] in ["AnswerQuestion","ReviseAnswer"]:
            call_id = tool_call["id"]
            search_queries = tool_call["args"].get("search_queries",[])

            #Execute each search query using th tavily tool

            query_results = {}

            for query in search_queries:
                result=tavily_tool.invoke(query)
                query_results[query]=result


            tool_messages.append(
                ToolMessage(
                    content=json.dumps(query_results),tool_call_id=call_id
                )
            )
    return tool_messages
