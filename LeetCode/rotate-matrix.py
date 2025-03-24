# Rotate Matrix/ Image - LeetCode 48
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

# DO NOT allocate another 2D matrix and do the rotation.
def reverse_list(lst):
    return lst[::-1]

def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            aux = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = aux     
        
        matrix[i] = reverse_list(matrix[i])
            
    return matrix


