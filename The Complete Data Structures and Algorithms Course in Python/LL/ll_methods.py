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
                pos += 1
                
            new_node.next = aux_pointer.next
            aux_pointer.next = new_node
        
            self.length += 1
            
        return True
    
    def traverse(self):
        current = self.head
        
        while current is not None:
            print(current.value)
            current = current.next
            
    def search(self, value):
        current = self.head
        
        while current is not None:
            if current.value == value:
                return True
            
            current = current.next
            
        return False
    
    def get(self, index):
        if index >= self.length or index < 0:
            return None
        else:
            pos = 0
            aux_node = self.head
            
            while pos != index:
                aux_node = aux_node.next
                pos += 1
            
            return aux_node
        
    def set(self, value, index):
        temp = self.get(index)
        
        if temp:
            temp.value = value
            
            return True

        return False
    
    def pop_first(self):
        if self.length > 0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            
            if self.head == None:
                self.tail = None
            
            return temp
        else:
            return None
        
    def pop(self):
        if self.length == 0:
            return None
        else:
            popped_node = self.tail
            
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                aux_node = self.get(self.length - 2)
                aux_node.next = None
                self.tail = aux_node
            
            self.length -= 1
            
            return popped_node
        
    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            aux_node = self.get(index - 1)
            
            removed_node = aux_node.next
            aux_node.next = removed_node.next
            removed_node.next = None
            
            self.length -= 1
            
            return removed_node
        
    def delete(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        list_str = ""
        
        temp_node = self.head
        
        while temp_node is not None:
            list_str += str(temp_node.value)
            
            if temp_node.next is not None:
                list_str += " -> "
                
            temp_node = temp_node.next
            
        return list_str
    
