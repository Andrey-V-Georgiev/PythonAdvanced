from collections import deque

text = input()
brackets = deque()

for i in range(len(text)):
    if text[i] == "(":
        brackets.append(i)
    elif text[i] == ")":
        start_index = brackets.pop()
        end_index = (i + 1)
        print(text[start_index: end_index])
