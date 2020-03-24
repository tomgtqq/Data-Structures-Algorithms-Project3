def sort_012(input_list=None):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if type(input_list) is not list or input_list is None or len(input_list) == 0:
        print("Please check input")
        return

    if len(input_list) == 1:
        return input_list

    start = 0
    end = len(input_list) - 1
    curr = 0

    while curr <= end:
        if input_list[curr] == 0:
            input_list[curr] = input_list[start]
            input_list[start] = 0
            start += 1
            curr += 1
        elif input_list[curr] == 2:
            input_list[curr] = input_list[end]
            input_list[end] = 2
            end -= 1
        else:
            curr += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Edge case
sort_012([])  # Should return "Please check input"
sort_012()  # Missing "input_list",Should return "Please check input"
test_function([1])  # Should return "Pass"
