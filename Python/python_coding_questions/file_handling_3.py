'''
Question: Find and Replace Text in a File

Write a Python program to find a specific word in a text file and replace it with another word. The changes should be saved back to the same file.

For example:

    Input file content:

This is a sample file.
File handling is interesting.

Replace file with document.

Output file content:

    This is a sample document.
    Document handling is interesting.

Let me know when you're ready with your solution or need any guidance! 😊'''
import os
def replace_word(input_file, keyword_find, keyword_replace):

    if not os.path.exists(input_file):
        print(f"The input file does not exist: {input_file}")
        return 
    with open(input_file, 'r') as f:
        content = f.read().lower()
    
    content = content.replace(keyword_find, keyword_replace)
    
    with open(input_file, 'w') as w:
        w.write(content)


input_file = "new.txt"
keyword_find = "file"
keyword_replace = "Document"
replace_word(input_file, keyword_find, keyword_replace)