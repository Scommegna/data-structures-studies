"""
Your task is to implement the binary_to_decimal method for the LinkedList class. This method should convert a binary number, represented as a linked list, to its decimal equivalent.

In this context, a binary number is a sequence of 0s and 1s. The LinkedList class represents this binary number such that each node in the linked list contains a single digit (0 or 1) of the binary number, and the whole number is formed by traversing the linked list from the head to the end.

The binary_to_decimal method should start from the head of the linked list and use each node's value to calculate the corresponding decimal number. The formula to convert a binary number to decimal is as follows:

To put it in simple terms, each digit of the binary number is multiplied by 2 raised to the power equivalent to the position of the digit, counting from right to left starting from 0, and all the results are summed together to get the decimal number.

The binary_to_decimal method should return this calculated decimal number.
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
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(" -> ".join(values)) 

    def binary_to_decimal(self):
        temp = self.head
        num = 0
        size = self.length - 1
        
        while temp:
            num += temp.value * pow(2, size)
            size -= 1
            temp = temp.next
            
        return num