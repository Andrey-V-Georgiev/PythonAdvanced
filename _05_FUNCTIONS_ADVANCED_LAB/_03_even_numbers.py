def filter_even_only(*args):
    filtered_list = filter(lambda x: x % 2 == 0, args[0])
    return filtered_list


input_string = input()
input_numbers = map(int, input_string.split(' '))
even_list = list(filter_even_only(input_numbers))
print(even_list)
