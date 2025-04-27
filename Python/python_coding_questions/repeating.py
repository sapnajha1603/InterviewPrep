'''
Question: Find the First Non-Repeating Character

Task: Write a Python function to find the first character in a string that does not repeat.
Example Input and Output:

    Input: "swiss"
    Output: 'w'

Requirements:

    Ignore spaces.
    If all characters repeat, return None.

Would you like to attempt this or see the solution?'''

from collections import Counter

def first_non_repeating(input_str):
    count = Counter(input_str.replace(" ", ""))

    for key, value in count.items():
        if value == 1:
            return key
    return None

inp ="swiss"
out_str = first_non_repeating(inp)
print(out_str)
    
