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
    
    # Pop method: deletes last item of LL and returns it
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.head
        actual_node = self.head
        
        while temp.next:
            actual_node = temp
            temp = temp.next
            
        self.tail = actual_node
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
        
        return temp