def layout(N, C, L):
    # Build adjacency list for restrictions
    restrictions = {i: set() for i in range(N)}
    for x, y in L:
        restrictions[x].add(y)
        restrictions[y].add(x)

    assignment = {}  # guest -> table

    def is_valid(guest, table):
        # Check if assigning this guest to this table causes conflict
        for other in restrictions[guest]:
            if other in assignment and assignment[other] == table:
                return False
        return True

    def backtrack(guest):
        # If all guests are assigned, return True
        if guest == N:
            return True

        for table in range(C):
            if is_valid(guest, table):
                assignment[guest] = table
                if backtrack(guest + 1):
                    return True
                # Backtrack
                del assignment[guest]

        return False

    # Start assigning from guest 0
    if backtrack(0):
        return assignment
    else:
        return False
N = 4
C = 2
L = [(0, 1), (1, 2), (2, 3)]

result = layout(N, C, L)
print(result)
 
