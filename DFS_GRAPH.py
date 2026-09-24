class DFSGraph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, bidirectional=True):
        """Adds an edge between vertex u and vertex v."""
        if u not in self.adj_list: self.adj_list[u] = []
        if v not in self.adj_list: self.adj_list[v] = []
        
        self.adj_list[u].append(v)
        if bidirectional:
            self.adj_list[v].append(u)

    def dfs(self, start_node):
        """Explores paths as deep as possible using Recursion."""
        if start_node not in self.adj_list:
            return []

        visited = set()
        traversal_order = []

        def _dfs_helper(node):
            visited.add(node)
            traversal_order.append(node)
            
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    _dfs_helper(neighbor)

        _dfs_helper(start_node)
        return traversal_order

# --- Run DFS ---
if __name__ == "__main__":
    g = DFSGraph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'E')

    print("DFS Traversal Order:", g.dfs('A'))
    # Output: ['A', 'B', 'D', 'E', 'C']
