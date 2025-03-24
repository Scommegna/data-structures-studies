class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        
    def prepend(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
        
    def insert(self, value, position):
        if position >= self.length or position < 0:
            return False
        
        if position == 0:
            self.prepend(value)
        elif position == self.length - 1:
            self.append(value)
        else:
            new_node = Node(value)
    
            aux_pointer = self.head
            pos = 0
            
            while pos != position - 1:
                aux_pointer = aux_pointer.next
                
            new_node.next = aux_pointer.next
            aux_pointer.next = new_node
        
            self.length += 1
            
        return True
    
    def traverse(self):
        current = self.head
        
        while current is not None:
            print(current.value)
            current = current.next
        
    def __str__(self):
        list_str = ""
        
        temp_node = self.head
        
        while temp_node is not None:
            list_str += str(temp_node.value)
            
            if temp_node.next is not None:
                list_str += " -> "
                
            temp_node = temp_node.next
            
        return list_str
    
