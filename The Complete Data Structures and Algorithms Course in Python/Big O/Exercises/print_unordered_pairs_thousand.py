"""
What is the runtime of the below code?
"""
# O(n * m)
def printUnorderedPairs(arrA, arrB):
    for i in range(len(arrA)):
        for j in range(len(arrB)):
            for k in range(0, 100000):
                print(str(arrA[i]) + "," + str(arrB[j]))
            
                