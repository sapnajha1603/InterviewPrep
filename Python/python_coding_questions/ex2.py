'''
Task: Write a Python function to generate all combinations of a given list of numbers of a specified length.
Example Input and Output:

    Input: numbers = [1, 2, 3], length = 2
    Output: [[1, 2], [1, 3], [2, 3]]'''

from itertools import combinations

def generate_combinations(inp_numbers, length):
    return list(combinations(inp_numbers, length))

numbers = [1, 2, 3]
length = 2
combination_list = generate_combinations(numbers, length)
print(combination_list)