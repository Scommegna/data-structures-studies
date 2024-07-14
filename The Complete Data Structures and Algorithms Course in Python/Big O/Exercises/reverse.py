"""
What is the runtime of the below code?
"""

# O(n)
def reverse(arr):
    for i in range(0, int(len(arr) / 2)):
        other = len(arr) - i - 1
        temp = arr[i]
        arr[i] = arr[other]
        arr[other] = temp
    
    print(arr)