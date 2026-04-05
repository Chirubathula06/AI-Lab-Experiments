from collections import deque

# Goal state
goal_state = "123456780"   # 0 = blank tile

# Moves: up, down, left, right
moves = {
    'up': -3,
    'down': 3,
    'left': -1,
    'right': 1
}

# Function to print puzzle
def print_state(state):
    for i in range(0, 9, 3):
        row = state[i:i+3]
        print(" ".join(x if x != "0" else "_" for x in row))
    print()

# Check if move is valid
def can_move(pos, move):
    if move == 'left' and pos % 3 == 0:
        return False
    if move == 'right' and pos % 3 == 2:
        return False
    if move == 'up' and pos < 3:
        return False
    if move == 'down' and pos > 5:
        return False
    return True

# BFS to solve puzzle
def solve(start_state):
    queue = deque([(start_state, [])])  # (state, path)
    visited = set([start_state])

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path + [state]

        pos = state.index("0")  # find blank position

        for move, step in moves.items():
            if can_move(pos, move):
                new_pos = pos + step
                new_state = list(state)
                # Swap blank with the tile
                new_state[pos], new_state[new_pos] = new_state[new_pos], new_state[pos]
                new_state = "".join(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [state]))
    return None


# Main Program
if __name__ == "__main__":
    # Example starting state
    start_state = "125340678"   # 0 = blank

    print("Initial State:")
    print_state(start_state)

    solution = solve(start_state)

    if solution:
        print("Solution found in", len(solution)-1, "moves:")
        for step in solution:
            print_state(step)
    else:
        print("No solution exists.")
