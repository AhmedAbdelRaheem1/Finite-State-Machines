# Import necessary libraries
import networkx as nx
import matplotlib.pyplot as plt

# Define states and transitions for the Finite State Machine (FSM)
states = ['S0', 'S1', 'S2', 'S3', 'S4']
transitions = {
    'S0': {'0': 'S1', '1': 'S2'},
    'S1': {'0': 'S3', '1': 'S4'},
    'S2': {'0': 'S4', '1': 'S3'},
    'S3': {'0': 'S2', '1': 'S1'},
    'S4': {'0': 'S0', '1': 'S0'}
}

# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from(states)

# Add edges to the graph representing transitions between states
for from_state, transitions_dict in transitions.items():
    for input_symbol, to_state in transitions_dict.items():
        G.add_edge(from_state, to_state, label=input_symbol)

# Function to find cycles in the graph
def find_circuits(graph):
    circuits = []
    visited = set()
    stack = []

    # Depth-first search to find cycles
    def dfs(node, circuit):
        nonlocal circuits, visited, stack

        visited.add(node)
        stack.append(node)
        circuit.append(node)

        for neighbor in graph[node]:
            if neighbor in visited and neighbor in stack:
                circuits.append(circuit + [neighbor])
            elif neighbor not in visited:
                dfs(neighbor, circuit[:])

        visited.remove(node)
        stack.remove(node)

    # Start DFS from each node in the graph
    for node in graph:
        dfs(node, [])

    return circuits

# Layout the nodes of the graph
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(8, 6))

# Draw nodes, edges, and labels
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='skyblue')
nx.draw_networkx_edges(G, pos, edge_color='black', arrows=True)
nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')

# Add labels for edges
edge_labels = {(n1, n2): d['label'] for n1, n2, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Set title and turn off axis
plt.title('Finite State Machine (FSM) Graph')
plt.axis('off')

# Show the graph
plt.show()
