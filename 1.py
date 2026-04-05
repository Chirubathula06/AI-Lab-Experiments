from collections import deque

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Depth First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()          # set to store visited nodes
    visited.add(start)           # mark current node as visited
    print(start, end=' ')        # print the node

    for neighbor in graph[start]:  # visit all neighbors
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Breadth First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Main driver
print("Graph traversal using DFS:")
dfs(graph, 'A')  # ✅ Pass a string, not a set

print("\nGraph traversal using BFS:")
bfs(graph, 'A')
