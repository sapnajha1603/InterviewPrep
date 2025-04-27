'''
Question: Sorting with Custom Rules

Task: Write a Python function to sort a list of strings based on the following custom rules:

    Strings that start with a vowel should appear before strings that start with a consonant.
    Strings should be sorted alphabetically within their respective groups (vowels first, then consonants).

Example Input and Output:

    Input: ["apple", "orange", "banana", "umbrella", "grape", "egg"]
    Output: ["apple", "egg", "orange", "umbrella", "banana", "grape"]'''

def sort_list(input_list):
    vowels = "aeiouAEIOU"
    vowels_list = []
    consonant_list = []
    total = []
    for string in input_list:
        if string[0] in vowels:
            vowels_list.append(string)
        else:
            consonant_list.append(string)
    total = sorted(vowels_list) + sorted(consonant_list)
    print(vowels_list)
    print(consonant_list)
    print(total)


input_list = ["apple", "orange", "banana", "umbrella", "grape", "egg"]
sort_list(input_list)