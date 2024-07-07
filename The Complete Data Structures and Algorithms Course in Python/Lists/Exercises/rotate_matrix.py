"""
Rotate Matrix/ Image - LeetCode 48
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

DO NOT allocate another 2D matrix and do the rotation.
"""

def rotate(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            
    for row in matrix:
        row.reverse()
            
            
rotate([[1,2,3],[4,5,6],[7,8,9]])