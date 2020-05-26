def print_args(*args):
    abs_values_list = [abs(num) for num in args[0]]
    print(abs_values_list)


input_str = input()
num_list = list(map(float, input_str.split(' ')))
print_args(num_list)
