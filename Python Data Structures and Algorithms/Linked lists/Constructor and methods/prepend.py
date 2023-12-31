class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    # Prepends new node to LL
    def prepend(self, value):
        node = Node(value)
        
        if self.length == 0:
            self.tail = node
            self.head = node
            
        else:
            node.next = self.head
            self.head = node
            
        self.length += 1
            
        return True