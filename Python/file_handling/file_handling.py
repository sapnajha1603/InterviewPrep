"""
Question: Write a Python script to rename all .txt files in a directory by appending _backup to their filenames.
Concepts Tested: File handling, loops, and the os module.

os.getcwd - will give you the path of the current working directory
os.listdir() - will give you the list of items in the current working directory
"""
import os

current_dir = os.getcwd()
print(f"The current working dir is: {current_dir}")



for i in range(1, 5):
    file_name = f"{i}.txt"
    # file_path = os.path.join(current_dir, file_name)
    file_path = current_dir/file_name
    file_path.touch()
    # with open(file_path, 'w') as f:
    #     f.write(f"This is the file{file_name}")



items = os.listdir(current_dir)
print(f"The items in the current dir are: {items}")

for item in items:
    print(item)