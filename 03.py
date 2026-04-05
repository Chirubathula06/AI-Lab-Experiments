import math
import random

# Function to minimize
def f(x):
    return x ** 2

# Simulated Annealing Algorithm
def simulated_annealing():
    current = random.uniform(-10, 10)  # Start at random point
    temperature = 100  # Initial temperature
    cooling_rate = 0.95  # Cooling rate

    while temperature > 0.01:
        new = current + random.uniform(-1, 1)  # New candidate solution

        # Calculate energy difference
        cost_change = f(new) - f(current)

        # Accept new if better OR with some probability
        if cost_change < 0 or random.random() < math.exp(-cost_change / temperature):
            current = new

        temperature *= cooling_rate  # Reduce temperature

    return current

# Run the algorithm
best_solution = simulated_annealing()
print("Best solution found:", best_solution)
print("Minimum value f(x):", f(best_solution))
