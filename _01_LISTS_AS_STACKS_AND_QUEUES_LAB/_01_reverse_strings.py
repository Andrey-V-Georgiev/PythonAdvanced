from collections import deque

text_queue = deque(input())
reverse_queue = deque()

for i in range(len(text_queue)):
    reverse_queue.append(text_queue.pop())

print("".join(reverse_queue))
