input_list = list(map(int, input().split(' ')))
even_list = list(filter(lambda num: num % 2 == 0, input_list))

print(even_list)
