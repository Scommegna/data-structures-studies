"""
You are given a singly linked list and two integers start_index and end_index.

Your task is to write a method reverse_between within the LinkedList class that reverses the nodes of the linked list from start_index to  end_index (inclusive using 0-based indexing) in one pass and in-place.

Note: the Linked List does not have a tail which will make the implementation easier.

Assumption: You can assume that start_index and end_index are not out of bounds.



Input

The method reverse_between takes two integer inputs start_index and end_index.

The method will only be passed valid indexes (you do not need to test whether the indexes are out of bounds)



Output

The method should modify the linked list in-place by reversing the nodes from start_index to  end_index.

If the linked list is empty or has only one node, the method should return None.



Example

Suppose the linked list is 1 -> 2 -> 3 -> 4 -> 5, and start_index = 2 and end_index = 4. Then, the method should modify the linked list to 1 -> 2 -> 5 -> 4 -> 3 .



Constraints

The algorithm should run in one pass and in-place, with a time complexity of O(n) and a space complexity of O(1).
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index, end_index):
        if self.length < 2:
            return None
            
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        counter = 0
        
        while counter != start_index:
            prev = prev.next
            counter += 1
            
        current = prev.next
        counter = 0
        
        while counter != end_index - start_index:
            moving_node = current.next
            current.next = moving_node.next
            moving_node.next = prev.next
            prev.next = moving_node
            
            counter += 1
            
        self.head = dummy.next
