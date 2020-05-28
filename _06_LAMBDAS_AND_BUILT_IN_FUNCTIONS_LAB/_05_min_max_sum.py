from collections import deque
from functools import reduce

input_list = deque(map(int, input().split(' ')))
_min = reduce(lambda a, b: a if a < b else b, input_list)
_max = reduce(lambda a, b: a if a > b else b, input_list)
_sum = reduce(lambda a, b: a + b, input_list)
print(f'The minimum number is {_min}')
print(f'The maximum number is {_max}')
print(f'The sum number is: {_sum}')

