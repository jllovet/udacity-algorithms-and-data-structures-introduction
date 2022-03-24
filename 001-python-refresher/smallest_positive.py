def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    smallest_positive = None
    for num in in_list:
        if num <= 0:
            continue
        if smallest_positive == None and len(in_list) != 0:
            smallest_positive = num
        elif smallest_positive > num:
            smallest_positive = num
    return smallest_positive

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-6, -9, -7]))
# Correct output: None

print(smallest_positive([]))
# Correct output: None

print(smallest_positive([88.22, -17.41, -26.53, 18.04, -44.81, 7.52, 0.0, 20.98, 11.76]))
# Correct output: 7.52