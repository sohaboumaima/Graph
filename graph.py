class Graph:

    # Initialize the graph.
    def __init__(self):
        self.g = {}

    # Return the list of nodes in the graph.
    def get_node_list(self):
        # To be implemented
        pass

    # Return the list of neighbors of a node.
    def get_neighbors(self, node):
        # To be implemented
        pass

    # Return list of edges in the form (i, j).
    def get_edge_list(self):
        # To be implemented
        pass

    # Add a new node to the graph.
    def add_node(self, v):
        # To be implemented
        pass

    # Check if a node is in the graph.
    def is_in_graph(self, v):
        # To be implemented
        pass

    # Delete edge
    def del_edge(self, v, w):
        # To be implemented
        pass

    # Delete node from the graph
    def del_node(self, v):
        for k in self.g[v]:
            self.g[k].remove[v]
        del self.g[v]

    # Add edge connecting the nodes v and w
    def add_edge(self, v, w):
        self.g[v].append(w)
        self.g[w].append(v)






