class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def contains(self, value):
        if self.root is None:
            return False
            
        temp = self.root
        
        while temp is not None:
            if temp.value == value:
                return True
            
            if value < temp.value:
                temp = temp.left
            
            if value > temp.value:
                temp = temp.right
            
        return False