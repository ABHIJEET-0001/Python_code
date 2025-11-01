import os

# Specify the path (you can also use '.' for current directory)
path = '/New folder'

try:
    # List all files and directories in the given path
    contents = os.listdir(path)

    print(f"Contents of directory '{path}':")
    for item in contents:
        print(item)


