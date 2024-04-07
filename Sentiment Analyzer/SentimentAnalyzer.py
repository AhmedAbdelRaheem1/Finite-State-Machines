# Define a class for the state machine
class StateMachine:

    # Initialize the state machine
    def __init__(self):
        # Dictionary to store handlers for each state
        self.handlers = {}
        # Variable to store the starting state
        self.startState = None
        # List to store end states
        self.endStates = []

    # Method to add a state to the state machine
    def add_state(self, name, handler, end_state=0):
        # Convert state name to uppercase for consistency
        name = name.upper()
        # Store the handler for the state
        self.handlers[name] = handler
        # If the state is an end state, add it to the list
        if end_state:
            self.endStates.append(name)

    # Method to set the starting state of the state machine
    def set_start(self, name):
        # Convert state name to uppercase for consistency
        self.startState = name.upper()

    # Method to run the state machine with input cargo
    def run(self, cargo):
        try:
            # Get the handler for the starting state
            handler = self.handlers[self.startState]
        except:
            # Raise an error if starting state is not set
            raise InitializationError("must call .set_start() before .run()")
        # Raise an error if there are no end states defined
        if not self.endStates:
            raise InitializationError("at least one state must be an end_state")

        # Loop until an end state is reached
        while True:
            # Execute the handler for the current state
            (newState, cargo) = handler(cargo)
            # If the new state is an end state, print and break the loop
            if newState.upper() in self.endStates:
                print("reached ", newState)
                break
            else:
                # Otherwise, get the handler for the new state
                handler = self.handlers[newState.upper()]

# Define lists of positive and negative adjectives
positive_adjectives = ["great", "nice", "fun", "entertaining", "suitable"]
negative_adjectives = ["boring", "worthless", "repetitive", "bad"]

# Define handler function for the start state
def start_transitions(txt):
    # Split the text into words
    splitted_txt = txt.split(None,1)
    # Extract the first word
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    # Transition to the 'Movie_state' if the first word is 'Movie'
    if word == "Movie":
        newState = "Movie_state"
    else:
        # Otherwise, transition to the 'error_state'
        newState = "error_state"
    return (newState, txt)

# Define handler function for the 'Movie_state'
def Movie_state_transitions(txt):
    # Split the text into words
    splitted_txt = txt.split(None,1)
    # Extract the first word
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    # Transition to the 'is_state' if the first word is 'is'
    if word == "is":
        newState = "is_state"
    else:
        # Otherwise, transition to the 'error_state'
        newState = "error_state"
    return (newState, txt)

# Define handler function for the 'is_state'
def is_state_transitions(txt):
    # Split the text into words
    splitted_txt = txt.split(None,1)
    # Extract the first word
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    # Transition based on the first word
    if word == "not":
        newState = "not_state"
    elif word in positive_adjectives:
        newState = "positive_state"
    elif word in negative_adjectives:
        newState = "negative_state"
    else:
        # Transition to the 'error_state' for unrecognized words
        newState = "error_state"
    return (newState, txt)

# Define handler function for the 'not_state'
def not_state_transitions(txt):
    # Split the text into words
    splitted_txt = txt.split(None,1)
    # Extract the first word
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    # Transition based on the first word
    if word in positive_adjectives:
        newState = "negative_state"
    elif word in negative_adjectives:
        newState = "positive_state"
    else:
        # Transition to the 'error_state' for unrecognized words
        newState = "error_state"
    return (newState, txt)
