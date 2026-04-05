import random

def objective(x):
    return -x**2 + 4*x

def hill_climb():
    x = random.uniform(-10, 10)
    step_size = 0.01
    while True:
        current = objective(x)
        next_x = x + step_size
        if objective(next_x) > current:
            x = next_x
        else:
            break
    return x, objective(x)

def main():
    x, val = hill_climb()
    print(f"Best solution: x = {x:.2f}, f(x) = {val:.2f}")

if __name__ == "__main__":
    main()
