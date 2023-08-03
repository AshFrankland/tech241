import os

os.system('echo Hello World!')

parent_dir = 'C:/Users/ashle/OneDrive/Documents/Sparta/Sparta Code/tech241/python_scripting'

directory = 'test_dir'

path = os.path.join(parent_dir, directory)

# os.mkdir(path)

# Putting a new file in the new dir

# filename = "testfile.txt"
# filepath = os.path.join(path, filename)
#
# with open(filepath, "w") as file1:
#     toFile = "Contents of file is written here"
#     file1.write(toFile)
#
# print("File " + filename + " created in " + directory + " folder")
