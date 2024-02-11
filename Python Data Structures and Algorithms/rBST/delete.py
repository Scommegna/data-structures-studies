class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

          
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node    

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value)  


    def min_value(self, current_node):
        while (current_node.left is not None):
            current_node = current_node.left
        return current_node.value 

    def delete_node(self, value):
        
        
    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
            
        if value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
            
        
            
        return current_node