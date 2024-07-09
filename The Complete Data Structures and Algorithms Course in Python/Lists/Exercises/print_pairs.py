"""
What is the runtime of the below code?
"""

# O(nˆ2)
def printPairs(arr):
    for i in arr:
        for j in arr:
            print(str(i)+","+str(j))