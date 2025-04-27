'''
Question: Find Duplicates in a List

Task: Write a Python function to find all duplicate elements in a given list.
Example Input and Output:

    Input: [1, 2, 3, 1, 2, 4, 5]
    Output: [1, 2]'''
from collections import Counter
def duplicates(inputlist):
    counter_1 = Counter(inputlist)
    repeat = []

    for key, value in counter_1.items():
        if value > 1:
            repeat.append(key)
    return repeat

Input = [1, 2, 3, 1, 2, 4, 5]
output_list = duplicates(Input)
print(output_list)

