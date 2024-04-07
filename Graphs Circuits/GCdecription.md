# Introduction

Detecting circuits in graphs is vital in diverse fields like computer science and biology. To efficiently find these loops, integrating Finite State Machines (FSMs) offers a promising approach. FSMs provide a structured framework that can systematically explore graphs to identify circuits. This solution aims to merge graph theory principles with FSM capabilities to develop efficient circuit detection algorithms, contributing to network analysis, system optimization, and understanding complex interconnected systems. (Siregar, 2020)

## Methodology

### Defining States and Transitions

- The “states” list contains the names of the states in the FSM.
- The “transitions” dictionary represents transitions between states based on input symbols. Each state has a dictionary mapping input symbols ('0' and '1') to the next state it transitions to.

### Creating the Graph

- The code initializes a directed graph (G) using NetworkX.
- Nodes corresponding to the states are added to the graph using “G.add_nodes_from(states)”.
- Edges representing transitions between states are added to the graph using “G.add_edge()”. Each edge is labeled with the input symbol that triggers the transition.

### Finding Circuits in the FSM

- The “find_circuits” function implements a depth-first search (DFS) algorithm to identify circuits in the FSM. A circuit is a closed loop that starts and ends at the same state.
- It initializes an empty list "circuit" to store identified circuits.
- The DFS function “dfs” traverses the graph, starting from each node/state.
- It marks visited nodes and maintains a stack to keep track of the current path being explored.
- If a node is visited and also in the stack, it denotes a circuit, and the function adds this “circuit” to the circuits list.
- The function “find_circuits” returns a list of identified circuits.

### Visualization of the FSM Graph

- The code uses Matplotlib to visualize the FSM graph.
- Positions of nodes are calculated using the spring layout algorithm (“pos = nx.spring_layout(G, seed=42)”).
- Nodes, edges, and labels are drawn on the plot using NetworkX functions (“nx.draw_networkx_nodes()”, “nx.draw_networkx_edges()”, “nx.draw_networkx_labels()”, “nx.draw_networkx_edge_labels()”).
- The resulting plot shows the FSM graph with labeled nodes, transitions, and the identified circuits (if any).

### Displaying Identified Circuits

- The code prints out the circuits found in the FSM using the “find_circuits” function.
