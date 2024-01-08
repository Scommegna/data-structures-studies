class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    # Removes first node of DLL and returns it
    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        
        if self.length == 1:
            self.head = None
            self.tail = None
            
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        
        self.length -= 1
        
        return temp