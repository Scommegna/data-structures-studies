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
    
    # Pops first node of LL  
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        
        self.head = self.head.next
        
        temp.next = None
        
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
            
        return temp