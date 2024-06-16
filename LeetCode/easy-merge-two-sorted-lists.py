"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        elif not list1 and not list2:
            return list2

        new_list = ListNode()
        pointer = new_list

        if list1.val <= list2.val:
            new_list.val = list1.val
            list1 = list1.next
        else:
            new_list.val = list2.val
            list2 = list2.next

        while list1 or list2:
            if list1 and list2:
                new_pointer = ListNode()

                if list1.val <= list2.val:
                    new_pointer.val = list1.val
                    list1 = list1.next
                else:
                    new_pointer.val = list2.val
                    list2 = list2.next

                pointer.next = new_pointer
                pointer = pointer.next
            elif list1 and not list2:
                new_node = ListNode(list1.val)
                pointer.next = new_node
                pointer = pointer.next
                list1 = list1.next
            else:
                new_node = ListNode(list2.val)
                pointer.next = new_node
                pointer = pointer.next
                list2 = list2.next

        return new_list