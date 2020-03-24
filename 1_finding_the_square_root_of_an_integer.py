def sqrt(number=None):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if type(number) is not int or type(number) is None:
        print('Please check input')
        return None

    if number < 0:
        print('The number must be a positive integer and 0')
        return None

    if number < 2:
        return number

    left = 2
    right = number // 2

    while left <= right:
        mid = left + (right - left) // 2
        num = mid * mid

        if num < number:
            left = mid + 1
        elif num > number:
            right = mid - 1
        else:
            return mid

    return right


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")

# Edge cases
sqrt("a")  # should print "Please check input"
sqrt()  # should print "Please check input"
sqrt(-1)  # should print "The number must be a positive integer and 0"
