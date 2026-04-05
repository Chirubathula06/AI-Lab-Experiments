def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} → {target}")
        return
    # Move n-1 disks from source to auxiliary
    hanoi(n - 1, source, auxiliary, target)
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} → {target}")
    # Move n-1 disks from auxiliary to target
    hanoi(n - 1, auxiliary, target, source)


# Example usage
n = int(input("Enter number of disks: "))
print(f"\nSteps to solve Towers of Hanoi with {n} disks:\n")
hanoi(n, 'A', 'C', 'B')
