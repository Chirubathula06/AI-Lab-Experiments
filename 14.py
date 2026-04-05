import random
import time
import itertools

# -------------------------
# Generate random items
# -------------------------
def generate_items(N):
    items = []
    for i in range(N):
        name = f"Item{i+1}"
        size = random.randint(1, 5)
        value = random.randint(1, 10)
        items.append((name, size, value))
    return items


# -------------------------
# Brute-force knapsack solver
# -------------------------
def knapsack_bruteforce(items, capacity):
    n = len(items)
    best_value = 0
    best_combination = []

    # Check all subsets of items
    for i in range(1, n + 1):
        for combo in itertools.combinations(items, i):
            total_size = sum(item[1] for item in combo)
            total_value = sum(item[2] for item in combo)
            if total_size <= capacity and total_value > best_value:
                best_value = total_value
                best_combination = combo

    return best_value, best_combination


# -------------------------
# Performance measurement
# -------------------------
def run_experiments():
    problem_sizes = [10, 12, 14, 16, 18, 20, 22]
    backpack_ratios = [1.0, 2.5, 4.0]

    for ratio in backpack_ratios:
        print(f"\n=== Testing with backpack size = {ratio} × N ===")
        for N in problem_sizes:
            times = []
            for _ in range(10):  # 10 runs
                items = generate_items(N)
                capacity = int(ratio * N)
                start = time.time()
                knapsack_bruteforce(items, capacity)
                end = time.time()
                times.append(end - start)

            avg_time = sum(times) / len(times)
            print(f"N = {N}, Avg time = {avg_time:.5f} seconds")


# Run the performance test
run_experiments()
