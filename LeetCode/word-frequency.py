# Count Word Frequency
# Define a function to count the frequency of words in a given list of words.

# Example:

# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
# count_word_frequency(words) 
# Output:

#  {'apple': 3, 'orange': 2, 'banana': 1}

def count_word_frequency(words):
    aux_dict = {}
    
    for item in words:
        if not item in aux_dict:
            aux_dict[item] = 1
        else:
            aux_dict[item] += 1
            
    return aux_dict
