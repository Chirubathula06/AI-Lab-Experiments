import itertools

def tsp_brute_force(graph):
    n = len(graph)
    cities = list(range(n))
    min_path = None
    min_cost = float('inf')

    for perm in itertools.permutations(cities[1:]):  # Fix the starting city as 0
        path = [0] + list(perm) + [0]  # start and end at city 0
        cost = 0
        for i in range(len(path) - 1):
            cost += graph[path[i]][path[i + 1]]
        if cost < min_cost:
            min_cost = cost
            min_path = path

    return min_path, min_cost

# Example distance matrix (graph[i][j] = distance from city i to city j)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, cost = tsp_brute_force(graph)
print("Minimum Cost Path:", path)
print("Total Cost:", cost)
