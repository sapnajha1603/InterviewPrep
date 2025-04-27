import os


for i in range(1, 71):
    dir_name = f"Tutorial_{i}"

    os.mkdir(dir_name)
 
    file_name = f"{i}.md"
    file_path = os.path.join(dir_name, file_name)
    # with open (file_path, "w") as f:
    #     f.write(f"Tutorial_{i} info down")
    