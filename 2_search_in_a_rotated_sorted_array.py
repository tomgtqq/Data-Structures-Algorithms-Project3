def rotated_array_search(input_list=None, number=None):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not (type(input_list) == list and type(number) == int):
        print("Please check input")
        return -1
    if input_list is None or len(input_list) == 0:
        print("Please check input")
        return -1

    left = 0
    right = len(input_list) - 1

    while left < right:
        midpoint = left + (right - left) // 2

        if input_list[midpoint] > input_list[right]:
            left = midpoint + 1   # The smallest value is in the right part
        else:
            right = midpoint      # The smallest value is in the left part

    start = right
    left = 0
    right = len(input_list) - 1

    if number >= input_list[start] and number <= input_list[right]:
        left = start
    else:
        right = start - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        if input_list[midpoint] == number:
            return midpoint
        elif input_list[midpoint] > number:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Edge cases
# missing "input_list", should return "Please check input"
rotated_array_search(number=10)
# missing "number", should return "Please check input"
rotated_array_search(input_list=[3, 1, 2])
# "input_list" is null , should return "Please check input"
rotated_array_search([], 10)
# "input_list" isn't array , should return "Please check input"
rotated_array_search(1, 10)
# "number" isn't integer, should return "Please check input"
rotated_array_search([3, 1, 2], 'a')
