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

# Returns node value of given index       
def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        value_to_be_found = self.head
        counter = 0
        
        while counter < index:
            value_to_be_found = value_to_be_found.next
            counter += 1
            
        return value_to_be_found