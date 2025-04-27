'''
Question 3: File Handling

Write a Python function that reads a text file line by line and writes only the lines that contain a specific keyword to a new file.

For example:

    Input file: input.txt

This is a test line.
Python is great for automation.
I love programming.
Automation is the future.

Keyword: "automation"
Output file: output.txt

Python is great for automation.
Automation is the future.'''

import os


def create_folder():

    if not os.path.exists("new"):
        os.mkdir("new")
        file_path = os.path.join("new", "input.txt")
        with open(file_path, 'w') as f:
            f.write("hello")
    
def filter_keyword_from_inp(input_file, output_file, keyword):
    
    if not os.path.exists(input_file):
        print(f"Error looking for file:\n {input_file}")
        print(f"Creating file: {input_file}")
        with open(input_file, 'w') as write_inp:
            write_inp.write("This is a test line.\n")
            write_inp.write("Python is great for automation.\n")
            write_inp.write("I love programming.\n")
            write_inp.write("Automation is the future.\n")

        
    with open(input_file, 'r') as infile:
        with open(output_file, 'w') as opfile:
            for line in infile:
                if keyword in line.lower():
                    opfile.write(line)

inp = "input.txt"
output = "output.txt"
keyword = "automation"
filter_keyword_from_inp(inp, output, keyword)
create_folder()