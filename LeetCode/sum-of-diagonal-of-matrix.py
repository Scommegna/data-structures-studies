# 2D Lists
# Given 2D list calculate the sum of diagonal elements.

# Example

# myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
# diagonal_sum(myList2D) # 15

def diagonal_sum(matrix):
    sum_of_elements = 0
    
    for i in range(len(matrix)):
        sum_of_elements += matrix[i][i]
        
    return sum_of_elements
