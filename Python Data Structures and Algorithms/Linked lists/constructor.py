# Class for node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Class for LL        
class LinkedList:
    def __init__(self, value):
        # Sets initial node, head and tail to first node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
my_list = LinkedList(4)

print(my_list.head.value) # prints first value