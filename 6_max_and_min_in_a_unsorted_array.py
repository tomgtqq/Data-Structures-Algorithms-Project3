def get_min_max(ints=None):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if type(ints) is not list or len(ints) == 0 or ints is None:
        print("Please check input")
        return

    smallest = ints[0]
    largest = ints[0]

    for index in range(1, len(ints)):
        if ints[index] < smallest:
            smallest = ints[index]
        if ints[index] > largest:
            largest = ints[index]

    return smallest, largest


# Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Edge case
l = [0, 0, 0, 0, 0, 0]
print("Pass" if ((0, 0) == get_min_max(l)) else "Fail")

get_min_max([])  # Should return "Please check input"
get_min_max()  # Should return "Please check input"
