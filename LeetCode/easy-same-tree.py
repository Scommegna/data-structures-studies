"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false


Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

class Solution:
    def dfs_in_order(self, node):
        if node is None:
            return []

        results = []

        def traverse(node):
            if node.left is not None:
                traverse(node.left)

            results.append(node.val)

            if node.right is not None:
                traverse(node.right)

        traverse(node)

        return results



    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = self.dfs_in_order(p)
        tree2 = self.dfs_in_order(q)

        if len(tree1) != len(tree2):
            return False
        else:
            for i in range(len(tree1)):
                if tree1[i] != tree2[i]:
                    return False

        return True