"""
Given a binary search tree, find the kth smallest element in the tree. For example, if the tree contains the elements [1, 2, 3, 4, 5], the 3rd smallest element would be 3.

The solution to this problem usually involves traversing the tree in-order (left, root, right) and keeping track of the number of nodes visited until you find the kth smallest element. There are two main approaches to doing this:

Iterative approach using a stack: This approach involves maintaining a stack of nodes that still need to be visited, starting with the leftmost node. At each step, you pop a node off the stack, decrement the kth smallest counter, and check whether you have found the kth smallest element. If you have not, you continue traversing the tree by moving to the right child of the current node.

Recursive approach: This approach involves recursively traversing the tree in-order and keeping track of the number of nodes visited until you find the kth smallest element. You can use a helper function that takes a node and a value of k as input, and recursively calls itself on the left and right children of the node until it finds the kth smallest element.

Both of these approaches have their own advantages and disadvantages, and the best approach to use may depend on the specific problem constraints and the interviewer's preferences.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def dfs_in_order(self):
        results = []
        
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            
            results.append(current_node.value)
            
            if current_node.right is not None:
                traverse(current_node.right)
                
        traverse(self.root)
        
        return results
        
    def kth_smallest(self, k):
        if self.root == None:
            return None
        
        res = self.dfs_in_order()
        
        if k > len(res):
            return None
            
        return res[k-1]
