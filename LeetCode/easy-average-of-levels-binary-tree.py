"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root, arr):
        if root is None:
            return

        queue = []
        queue.append(root)

        while len(queue) > 0:
            val = 0

            for node in queue:
                val += node.val
            
            arr.append((float) (val/len(queue)))

            length = len(queue)

            while length > 0:
                if queue[length - 1].left is not None:
                    queue.append(queue[length - 1].left)

                if queue[length - 1].right is not None:
                    queue.append(queue[length - 1].right)

                queue.pop(length - 1)

                length -= 1

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        arr = []

        self.bfs(root, arr)

        return arr