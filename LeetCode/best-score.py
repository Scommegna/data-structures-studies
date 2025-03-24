# Best Score
# Given a list, write a function to get first, second best scores from the list.

# List may contain duplicates.

# Example

# myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# first_second(myList) # 90 87

def first_second(my_list):
    aux_set = set(my_list)
    
    greatest = second_greatest = float('-inf')
    
    for num in aux_set:
        if num > greatest:
            second_greatest = greatest
            greatest = num
        elif num > second_greatest:
            second_greatest = num
            
    return (greatest, second_greatest)