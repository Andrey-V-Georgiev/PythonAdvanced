from os import path

path_str = './text.txt'
print('File found') if path.exists(path_str) else print('File not found')


