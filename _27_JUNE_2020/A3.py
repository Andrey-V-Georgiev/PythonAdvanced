
def list_manipulator(list_of_numbers, operation, command, *args):
    numbers = list(args)
    if operation == 'add' and command == 'beginning':
        for _ in range(len(numbers)):
            list_of_numbers.insert(0, numbers.pop())
    elif operation == 'add' and command == 'end':
        for _ in range(len(numbers)):
            list_of_numbers.append(numbers.pop(0))
    elif operation == 'remove' and command == 'beginning':
        if numbers:
            r_length = numbers[0]
            for _ in range(r_length):
                list_of_numbers.pop(0)
        else:
            list_of_numbers.pop(0)
    elif operation == 'remove' and command == 'end':
        if numbers:
            r_length = numbers[0]
            for _ in range(r_length):
                list_of_numbers.pop()
        else:
            list_of_numbers.pop()
    return list_of_numbers


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
