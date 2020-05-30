path_str = './numbers.txt'
file_obj = open(path_str, 'r')
sum_numbers = 0
for line in file_obj:
    sum_numbers += int(line)
print(sum_numbers)

