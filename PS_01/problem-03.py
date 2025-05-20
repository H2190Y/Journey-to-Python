import os

# Get the current directory or specify the directory you want to inspect
directory = '.'  # '.' refers to the current directory
# You can also specify a different directory, for example:
# directory = '/path/to/your/directory'

# Get the list of contents in the directory
contents = os.listdir()

# Print the contents of the directory
print("Contents of the directory:")
for item in contents:
    print(item)
