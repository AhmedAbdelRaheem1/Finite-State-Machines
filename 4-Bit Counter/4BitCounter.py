# Define a class for the Four Bit Counter Finite State Machine (FSM)
class FourBitCounterFSM:
    def __init__(self):
        # Define possible states of the FSM
        self.states = ['S0', 'S1', 'S2', 'S3']
        # Define transitions between states
        self.transitions = {
            'S0': 'S1',
            'S1': 'S2',
            'S2': 'S3',
            'S3': 'S0'
        }
        # Initialize current state to 'S0'
        self.current_state = 'S0'
        # Initialize count to 0
        self.count = 0

    # Method to transition to the next state
    def transition(self):
        # Update current state based on transition rules
        self.current_state = self.transitions[self.current_state]

    # Method to get the count in binary representation
    def get_count(self):
        # Format count as 4-bit binary representation
        binary_count = format(self.count, '04b')
        return binary_count

    # Method to increment the count
    def increment(self):
        # Increment count and ensure it stays within 4-bit range (0-15)
        self.count = (self.count + 1) % 16
