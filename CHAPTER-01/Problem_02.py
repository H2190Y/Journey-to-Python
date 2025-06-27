# Import the os module
import os

# Define the directory path you want to list
directory_path = '.'  # '.' means current directory

# Use os.listdir() to get a list of all files and folders in the directory
contents = os.listdir(directory_path)

# Print the contents
print(f"Contents of directory '{directory_path}':")
for item in contents:
    print(item)
