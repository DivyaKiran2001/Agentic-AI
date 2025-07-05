### Message Graph

It is a class that Langgraph provides that we can use to orchestrate the flow of messages between different nodes

**In Simple Terms** : MessageGraph maintains a list of messages and decides the flow of messages between nodes

- Every node in MessageGraph receives the full list of previous messages as input
- Each node can append new messages to the list and return it
- The updated message list is then passed to the next node

Example Use cases : Simple routing decisions,simple chatbot conversation flow

**NOTE** : If the app requires complex state management, we have StateGraph 
