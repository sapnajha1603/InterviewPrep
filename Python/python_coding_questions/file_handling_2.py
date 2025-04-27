'''
Question: Count Lines, Words, and Characters

Write a Python program to count the number of lines, words, and characters in a file.

Let me know when you're ready with your solution or need any guidance! 😊'''

import os

def count_line_word_characters(input_file):
    lines = 0
    words = 0
    characters = 0
    if not os.path.exists(input_file):
        print(f"Error looking for file: {input_file}")
        return
    with open(input_file, 'r') as line_ip:
        for line in line_ip:
            total_lines = line.split()
            lines += 1
            words += len(total_lines)
            characters += len(line.strip())
    print(f"The total number of lines are: {lines}")
    print(f"The total number of words are: {words}")
    print(f"The total number of characters are: {characters}")

input_file = "input.txt"
count_line_word_characters(input_file)

