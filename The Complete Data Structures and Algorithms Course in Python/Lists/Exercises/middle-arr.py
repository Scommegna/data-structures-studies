"""
Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

myList = [1, 2, 3, 4]
middle(myList)  # [2,3]
"""

def getMiddle(numberList): 
    return numberList[1 : -1]
