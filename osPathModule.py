import os

#it takes two or more paths and join them
print(os.path.join('Users/File/Input','Users/File'))

#it provides absolute name of the path
print(os.path.abspath('input.py'))

#it provides standard format name
print(os.path.normpath('../input.py'))

#it splits file into two paths directory path and filename
#print(os.path.split(" '''Some file path''' "))

#it gives idea if path exists or not
#print(os.path.exists(' """Some file path""" '))

# print(os.path.isdir(' """Directory""" '))

# print(os.walk(' Traversing the subfolders '))