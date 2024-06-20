"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

class Solution:
    def dfs(self, root, res, par):
        if root:
            if par == "left":
                res.append(root.val)

                self.dfs(root.left, res, par)
                self.dfs(root.right, res, par)
            else:
                res.append(root.val)

                self.dfs(root.right, res, par)
                self.dfs(root.left, res, par)
        else:
            res.append(None)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if (not root.left and root.right) or (root.left and not root.right):
            return False
        elif (root.left and root.right) and (root.left.val != root.right.val):
            return False

        left = []
        right = []

        self.dfs(root.left, left, "left")
        self.dfs(root.right, right, "right")

        if len(left) != len(right):
            return False

        for i in range(len(left)):
            if left[i] != right[i]:
                return False

        return True

        