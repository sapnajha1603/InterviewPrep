'''
Question: Find the Longest Common Prefix

Task: Write a Python function to find the longest common prefix among an array of strings. If there is no common prefix, return an empty string.
Example Input and Output:

    Input: ["flower", "flow", "flight"]

    Output: "fl"

    Input: ["dog", "racecar", "car"]

    Output: "" (no common prefix)'''

from collections import Counter

def longest_common_prefix(input_array):
    prefix = input_array[0]

    for string in input_array[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            while not prefix:
                return None
    print(f"The common prefix is : {prefix}")



inp = ["flower", "flow", "flight"]
longest_common_prefix(inp)
