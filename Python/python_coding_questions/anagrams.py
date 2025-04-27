'''
Question: Check for Anagrams

Task: Write a Python function to check if two strings are anagrams of each other. Two strings are anagrams if they contain the same characters with the same frequencies, but the order can be different.
Example Input and Output:

    Input: "listen", "silent"

    Output: True

    Input: "hello", "world"

    Output: False
    '''
from collections import Counter
def anagrams(string1, string2):
    counter_1 = Counter(string1)
    counter_2 = Counter(string2)

    return counter_1 == counter_2

inp1 = "listen"
inp2 = "silent"
print(anagrams(inp1,inp2))