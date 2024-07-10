"""
What is the runtime of the below code?
"""

# O(nˆ2)
def printUnorderedPairs(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            print(arr[i] + "," + arr[j])