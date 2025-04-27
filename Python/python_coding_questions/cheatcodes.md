1. to read a file
with open(file_name, 'r') as f:

2. to write into a file
with open(file_name, 'w') as f:
    f.write("input")

3. to check if  a file is present
import os
if os.path.exists(file_name)

4. to create a file and write content

if not os.path.exists(input_file):
    with open(file_name, 'w') as f:
        f.write("input")

5. to remove a file
if os.path.exists(input_file):
    os.remove(input_file)

6. to create a folder via python
os.mkdir("folder_name")

7. to create a file inside a folder
new_file = os.path.join(folder_name, file_name)
with open(new_file, 'w') as f:
    f.write("data") //if you dont do with open it will not create  any file

8. to remove new line charaters
line.strip()

9. To use counters in normal code
from collections import Counter

