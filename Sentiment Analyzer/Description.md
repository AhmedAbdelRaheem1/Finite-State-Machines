# Introduction

Sentiment analysis, a prominent application of natural language processing, has gained immense significance in understanding human emotions and opinions expressed in textual data. Implementing a simple sentiment analyzer using a Finite State Machine (FSM) offers an intriguing and effective approach to discerning sentiment from text. FSMs provide a structured model to analyze and classify text based on its emotional content. In this exploration, we will delve into the construction of a basic sentiment analyzer using FSMs, elucidating how this computational model can be leveraged to recognize and categorize sentiments, thereby unraveling the rudiments of sentiment analysis in a comprehensible manner.

## Methodology

### State Representation:

- States are represented by strings ("Start", "Movie_state", "is_state", “not_state”).
- Each state has an associated handler function that processes input based on the current state.

### State Transitions:

- The state transitions are defined by functions like ‘start_transitions’, ‘Movie_state_transitions’, ‘is_state_transitions’, and ‘not_state_transitions’.
- These functions take input (a text string), process it, and return a tuple containing the next state and the remaining text to be processed.

### Adding States and Handlers:

- The ‘add_state’ method in the StateMachine class is used to add states and their associated handler functions.
- ‘set_start’ sets the initial state for the FSM.

### Run the State Machine:

- The ‘run’ method executes the state machine. It starts with the initial state and iterates through the transitions based on the input text until it reaches an end state.

### End States:

- Certain states are designated as end states by passing ‘end_state=1’ when adding those states via ‘add_state method.’
- When the FSM reaches an end state, it stops processing and prints the reached state.

### Input Processing:

- The input text is processed in each state transition function by splitting the text based on spaces and examining the first word to determine the next state or action.
- Conditions based on specific words ("Movie", "is",”not” if exist, positive adjectives, or negative adjectives) determine the transitions between states.

### Handling Errors:

- If the input doesn't match any expected conditions in a state, it transitions to an "error_state".

### Execution:

- After setting up the states, the code executes the FSM for different input phrases like "Movie is great", "Movie is bad", and "Ahmed has slept", printing the reached states for each.
