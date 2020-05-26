def round_numbers(*args):
    return [round(num) for num in args[0]]


input_string = input()
input_numbers = map(float, input_string.split(' '))
rounded_numbers = round_numbers(input_numbers)
print(rounded_numbers)
