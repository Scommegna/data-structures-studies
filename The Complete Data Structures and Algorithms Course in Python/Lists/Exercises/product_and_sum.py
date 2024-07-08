"""
What is the runtime of the below code?
"""

#O(n) time complexity
def foo(arr):
    sum = 0
    prod = 1
    
    for i in arr:
        sum += i
        
    for i in arr:
        prod *= i
        
    print("Sum = "+str(sum)+", Product = "+str(prod))