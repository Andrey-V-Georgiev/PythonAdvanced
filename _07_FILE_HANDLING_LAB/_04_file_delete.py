import os

path = './my_first_file.txt'
try:
    os.remove(path)
except FileNotFoundError:
    print('File already deleted!')
