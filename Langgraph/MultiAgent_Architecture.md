**Multi-Agent Architectures**

- We know that an agent is a system that uses an LLM to decide the control flow of an application

- As you develop these systems,they might grow more complex over time,making them harder to manage and scale

- For Example,you might run into the following problems :

1. Agent has too many tools at its disposal and makes poor decisions about which tool to call next
2. Context grows too complex for a single agent to keep track of

 To tackle these , you might consider breaking your application into multiple smaller , independent agents and
 composing them into multi agent system.

 **Subgraphs**:

Subgraphs allow you to build complex systems with multiple components that are themselves graphs.A common use case for using subgraphs is 
building multi agent systems

=> The main question when adding subgraphs is how the parent graph and subgraph communicate i.e
how they pass the state between each other during the graph execution

There are two scenarios 

1. **Parent graph and subgraph share schema keys :** In this case, you can add a node with
   the compiled graph
2. **Parent graph and subgraph have different schemas :** In this case,you have to add a node function that invokes the subgraph this is
 useful when the parent graph and the subgraph have different state schemas and you need to transform state
before or after calling the subgraph
