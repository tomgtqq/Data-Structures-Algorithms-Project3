def rearrange_digits(input_list=None):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if type(input_list) is not list or input_list is None or len(input_list) == 0:
        print("Please check input")
        return

    sorted_list = heapsort(input_list)

    max_sum_1 = 0
    max_sum_2 = 0

    for i in range(0, len(sorted_list), 2):
        if i < len(sorted_list):
            max_sum_1 += sorted_list[i] * pow(10, i // 2)
        if i + 1 < len(sorted_list):
            max_sum_2 += sorted_list[i + 1] * pow(10, (i + 1) // 2)

    return max_sum_1, max_sum_2


def heapify(arr, n, i):

    largest_index = i
    left_node = 2 * i + 1
    right_node = 2 * i + 2

    if left_node < n and arr[i] < arr[left_node]:
        largest_index = left_node

    if right_node < n and arr[largest_index] < arr[right_node]:
        largest_index = right_node

    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]

        heapify(arr, n, largest_index)


def heapsort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

# Edge case
test_case = [[9, 9, 9, 9, 9], [999, 99]]
test_function(test_case)

test_case = [[1, 0, 0, 0, 0], [100, 0]]
test_function(test_case)

test_case = [[0, 0, 0, 0, 0], [0, 0]]
test_function(test_case)

# Check "input_list"

rearrange_digits()  # "input_list" missing, should return "Please check input"
rearrange_digits([]) # "input_list" is null, should return"Please check input"
