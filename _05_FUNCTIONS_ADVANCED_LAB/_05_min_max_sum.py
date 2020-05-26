def print_min_max_sum(*args):
    num_list = list(args[0])
    min_num = min(num_list)
    max_num = max(num_list)
    sum_num = sum(num_list)
    print(f'The minimum number is {min_num}')
    print(f'The maximum number is {max_num}')
    print(f'The sum number is: {sum_num}')


input_string = input()
input_numbers = map(int, input_string.split(' '))
print_min_max_sum(input_numbers)
