def fix_calendar(_numbers):
    numbers_length = len(_numbers)
    for i in range(numbers_length):
        for j in range(numbers_length - 1):
            num = _numbers[j]
            next_num = _numbers[j + 1]
            if num > next_num:
                _numbers[j], _numbers[j + 1] = next_num, num
    return _numbers


numbers = [3, 2, 1]
fixed = fix_calendar(numbers)
print(fixed)
