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

- 

- 
