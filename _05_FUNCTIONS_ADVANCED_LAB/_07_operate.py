def arithmetic_operations(operation, result, num_list):
    for num in num_list:
        if operation == '+':
            result += num
        elif operation == '-':
            result -= num
        elif operation == '*':
            result *= num
        elif operation == '/':
            result /= num
    return result


def operate(*args):
    args_data = list(args)
    operation = args_data[0]
    num_list = list(map(int, args_data[1:]))
    if operation == '+' or operation == '-':
        result = 0
        return arithmetic_operations(operation, result, num_list)
    elif operation == '*' or operation == '/':
        result = 1
        return arithmetic_operations(operation, result, num_list)


print(operate("+", 1, 2, 3))
