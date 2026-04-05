from queue import PriorityQueue
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(start, goal, graph):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {start: 0}
    
    while not frontier.empty():
        current = frontier.get()[1]
        
        if current == goal:
            break
        
        for next in graph[current]:
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put((priority, next))
                came_from[next] = current
                
    return came_from, cost_so_far

def main():
    graph = {
        (0,0): [(0,1), (1,0)],
        (0,1): [(0,0), (1,1)],
        (1,0): [(0,0), (1,1), (2,0)],
        (1,1): [(0,1), (1,0), (2,1)],
        (2,0): [(1,0), (2,1)],
        (2,1): [(2,0), (1,1)]
    }
    start, goal = (0,0), (2,1)
    path, cost = astar(start, goal, graph)
    print("Path found:", path)
    print(cost)

if __name__ == "__main__":
    main()

