def validate_num(number):
    result = False
    for d in range(2, 11):
        if number % d == 0:
            result = True
            break
    return result


start = int(input())
end = int(input())
output_list = [num for num in range(start, end + 1) if validate_num(num)]
print(output_list)
