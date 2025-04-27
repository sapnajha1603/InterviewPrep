'''
Question: Find the Maximum Occurring Character

Task: Write a Python function to find the character that appears the most in a given string. If there is a tie, return any one of the most frequent characters.
Example Input and Output:

    Input: "hello world"
    Output: 'l'
'''
from collections import Counter
def max_occuring(input_str):
    max_count = Counter(input_str.replace(" ", ""))
    max_value = max(max_count.values())
    for key, value in max_count.items():
        if max_value == value:
            return key
    

input_1 = "hello world"
op = max_occuring(input_1)
print(f"The max_occuring letter is : {op}")

        
