"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, arr):
        if root:
            if root.left is not None:
                self.dfs(root.left, arr)

            arr.append(root.val)

            if root.right is not None:
                self.dfs(root.right, arr)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []

        self.dfs(root, arr)

        diff = 0

        if len(arr) == 1:
            return diff
        else:
            pointer1 = 0
            pointer2 = 1

            diff = arr[pointer2] - arr[pointer1]

            while pointer2 < len(arr):
                if arr[pointer2] - arr[pointer1] < diff:
                    diff = arr[pointer2] - arr[pointer1]

                pointer2 += 1
                pointer1 += 1

            return diff