# Higher-order function: takes a function (test) and a list (lst)
def count(test, lst):
    # Base case: if the list is empty, no elements to check
    if lst == []:
        return 0

    # Recursive step: check the first element and move to the rest
    if test(lst[0]):
        return 1 + count(test, lst[1:])
    else:
        return count(test, lst[1:])
print(count(lambda x: x > 2, [1, 2, 3, 4, 5]))
