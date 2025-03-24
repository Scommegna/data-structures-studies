# Max Product of Two Integers
# Find the maximum product of two integers in an array where all elements are positive.

# Example

# arr = [1, 7, 3, 4, 9, 5] 
# max_product(arr) # Output: 63 (9*7)

def max_product(arr):
    greater = second_greater = float('-inf')

    for num in arr:
        if num > greater:
            second_greater = greater
            greater = num
        elif num > second_greater:
            second_greater = num

    return greater * second_greater