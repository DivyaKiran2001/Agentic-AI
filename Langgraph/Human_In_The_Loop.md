### Human In the Loop

- A human-in-the-loop workflow integrates human input into autonomous processes,allowing for decisions,validation or corrections
- at key stages

### Use Cases :
1. Reviewing tool calls
2. Validating LLM outputs
3. Providing context

### Human In the Loop (Design Patterns)

There are typically three different actions that you can do with a human-in-the-loop workflow :

1. **Approve or Reject :**

- Pause the graph before a critical step,such as an API call,to review and approve the action
- If the action is rejected, you can prevent the graph from executing the step,and potentially take an
- alternative action.This pattern often involve routing the graph based on the humans input

2. **Review and Edit State** :

- A human can review and edit the state of the graph
- This is useful for correcting mistakes or updating the state with additional information

3. **Review Tool calls** :

- A human can review and edit the output from the LLM before proceeding
- This is particularly critical in applications where the tool calls requested by
- the LLM may be sensitive or require human oversight

  
**Drawbacks of input()**:

- Freezes your program completely until someone types something
- Only works in terminals - useless for web apps
- If your program crashes,all progress is lost
- Lives only in your terminal session
- Can only handle one user at a time

So due to this we use a special method that LangGraph provides called "interrupt"

**What is interrupt()**:

- Special LangGraph function that pauses your workflow nicely
- Saves your program's state so it can continue later
- Works in web apps,APIs and other interfaces
- Handles multiple users/sessions at once
- Survives program crashes and restarts
- Lets humans take their time to respond
- Required for any serious human-in-the-loop system

### Operations with interrupt :

1. **Resume** : Continue execution with input from the user without modifying the state
2. **Update and Resume** : Update the state and then continue execution
3. **Rewind/Time Travel**: Go back to a previous checkpoint in the execution
4. **Branch** : Create a new branch from the current execution state to explore alternative paths
5. **Abort** : Cancel the current execution entirely

### Command Class :

The command class in LangGraph allows us to create edgeless workflows

Example Syntax :

def agent(state:MessageState) -> Command[Literal[...,END]]:
    return Command(
      goto= ....,
      update = {"messages":[response]}
    )

  
