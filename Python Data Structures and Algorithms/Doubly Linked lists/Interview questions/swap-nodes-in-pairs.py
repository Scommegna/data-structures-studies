"""
This question is acknowledged as one of the more intricate challenges within the Doubly Linked List section. It's not unusual for students to find this task quite formidable at this point in the course.

If you're considering diving into this problem, it's crucial to approach it methodically. I recommend drawing out the list structures and operations to better visualize the problem. This challenge demands a deep understanding of Doubly Linked Lists' unique characteristics and manipulation techniques.

Use this opportunity to deepen your understanding, but also remember it's absolutely fine to come back to this problem later if it feels overwhelming now. Progress in complex concepts like these sometimes requires stepping back and revisiting with fresh insights. Good luck, and remember that perseverance is key in mastering these advanced topics!

Now, here is the problem:

_________________________________



You are given a doubly linked list.

Implement a method called swap_pairs within the class that swaps the values of adjacent nodes in the linked list. The method should not take any input parameters.

Note: This DoublyLinkedList does not have a tail pointer which will make the implementation easier.

Example:

1 <-> 2 <-> 3 <-> 4 should become 2 <-> 1 <-> 4 <-> 3

Your implementation should handle edge cases such as an empty linked list or a linked list with only one node.

Note: You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes (i.e., only the nodes' prev and next pointers may be changed.)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    
    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        prev_node = dummy
        
        while self.head and self.head.next:
            first = self.head
            second = self.head.next
            
            prev_node.next = second
            first.next = second.next
            second.next = first
            
            second.prev = prev_node
            first.prev = second
            
            if first.next:
                first.next.prev = first
                
            self.head = first.next
            prev_node = first
            
        self.head = dummy.next
        
        if self.head:
            self.head.prev = None
