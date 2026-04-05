# Wumpus World - Final Correct World and Solution

world = {
    (1,1): "Safe",
    (2,1): "Stench",
    (3,1): "Wumpus",
    (4,1): "Stench",

    (1,2): "Breeze",
    (2,2): "Safe",
    (3,2): "Gold",
    (4,2): "Safe",

    (1,3): "Pit",
    (2,3): "Breeze",
    (3,3): "Pit",
    (4,3): "Breeze",

    (1,4): "Breeze",
    (2,4): "Safe",
    (3,4): "Breeze",
    (4,4): "Pit"
}

# safe to step if NOT pit or wumpus
def safe(cell):
    danger = ["Pit", "Wumpus"]
    return world.get(cell) not in danger

moves = [(1,0),(-1,0),(0,1),(0,-1)]
visited = set()
path = []

def dfs(cell):
    if cell in visited: return False
    visited.add(cell)
    path.append(cell)

    if world.get(cell) == "Gold":
        return True

    x,y = cell
    for dx,dy in moves:
        nxt = (x+dx, y+dy)
        if nxt in world and safe(nxt):
            if dfs(nxt):
                return True

    path.pop()
    return False

dfs((1,1))
print("Solution path:", path)
