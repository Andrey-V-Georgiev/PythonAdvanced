def print_sorted(*args):
    print(sorted(args[0]))


input_string = input()
input_numbers = map(int, input_string.split(' '))
print_sorted(input_numbers)
