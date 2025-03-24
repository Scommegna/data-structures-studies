# Key with the Highest Value
# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

# Example:

# my_dict = {'a': 5, 'b': 9, 'c': 2}
# max_value_key(my_dict))
# Output:

# b

def max_value_key(my_dict):
    greatest_key = ''
    greatest_val = float('-inf')
    
    for key, value in my_dict.items():
        if value > greatest_val:
            greatest_val = value
            greatest_key = key
            
    return greatest_key