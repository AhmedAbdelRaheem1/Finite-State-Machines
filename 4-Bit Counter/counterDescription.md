# Introduction

A finite state machine (FSM) is a computational model used to design and analyze sequential logic circuits. It consists of a set of states, transitions between states, and an initial state. In this project, we will implement a simple 4-bit counter using a finite state machine. A counter is a digital circuit that counts in binary from 0 to its maximum value. The 4-bit counter will count from 0000 to 1111 and then reset to 0000.

## Methodology using Python

### Initialization

- The “FourBitCounterFSM” class initializes with an initial state “S0”, which represents the state of the counter.
- It also initializes a dictionary “transitions” that maps each state to its next state in a cyclic manner: “S0” -> “S1” -> “S2” -> “S3” -> “S0”.
- The “count” variable is set to 0, representing the current count of the 4-bit counter.

### Transition Function

- The “transition” method is responsible for transitioning the counter from its current state to the next state based on the “transitions” dictionary.
- Each time “transition” is called, the current state is updated according to the predefined state transitions.

### Count Representation

- The “get_count” method returns the binary representation of the count with leading zeros to ensure a 4-bit representation. It uses the “format” function to achieve this.

### Incrementing the Counter

- The “increment” method increases the count by 1, simulating the addition of a binary number in a 4-bit space.
- The “% 16” operation ensures that the count wraps around from 15 to 0, mimicking a 4-bit overflow behavior.

### Execution

- The “for” loop iterates 16 times, printing the current count at each step by calling “get_count” and then incrementing the count using “increment”.
