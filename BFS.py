from collections import deque

class BFSGraph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, bidirectional=True):
        """Adds an edge between vertex u and vertex v."""
        if u not in self.adj_list: self.adj_list[u] = []
        if v not in self.adj_list: self.adj_list[v] = []
        
        self.adj_list[u].append(v)
        if bidirectional:
            self.adj_list[v].append(u)

    def bfs(self, start_node):
        """Explores neighbors layer by layer using a Queue."""
        if start_node not in self.adj_list:
            return []

        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        traversal_order = []

        while queue:
            current = queue.popleft()
            traversal_order.append(current)

            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return traversal_order

# --- Run BFS ---
if __name__ == "__main__":
    g = BFSGraph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'E')

    print("BFS Traversal Order:", g.bfs('A'))
    # Output: ['A', 'B', 'C', 'D', 'E']
