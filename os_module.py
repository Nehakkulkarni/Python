import os

print("Current working directory: ")
cwd = os.getcwd()
print(cwd)
print("List of files: ")
files = os.listdir()

for f in files:
    print(f)
print("Create new directory:")
folder = "new_folder"
if os.path.exists(folder):
    print("Folder already exists")
else:
    os.mkdir(folder)
    print("Folder created successfully")