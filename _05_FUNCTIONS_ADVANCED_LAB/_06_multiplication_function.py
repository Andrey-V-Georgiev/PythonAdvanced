def multiply(*args):
    num_list = list(args)
    result = 1
    for num in num_list:
        result *= num
    return result


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))


