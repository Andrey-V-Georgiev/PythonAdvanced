from collections import deque
from math import floor


def do_operation(_current_item, _tmp_deque):
    _tmp_result = float(_tmp_deque.popleft())
    if _current_item == '+':
        for num in _tmp_deque:
            _tmp_result += float(num)
    elif _current_item == '-':
        for num in _tmp_deque:
            _tmp_result -= float(num)
    elif _current_item == '*':
        for num in _tmp_deque:
            _tmp_result *= float(num)
    elif _current_item == '/':
        for num in _tmp_deque:
            _tmp_result /= float(num)
    return int(_tmp_result)


def print_result(final_result):
    print(floor(float(final_result)))


input_deque = deque(input().split())
operators = ("*", "+", "-", "/")
tmp_deque = deque()

while True:
    current_item = input_deque.popleft()
    if current_item in operators:
        tmp_result = do_operation(current_item, tmp_deque)
        if len(input_deque) == 0:
            print_result(tmp_result)
            break
        input_deque.appendleft(str(tmp_result))
        tmp_deque.clear()
    else:
        tmp_deque.append(current_item)



