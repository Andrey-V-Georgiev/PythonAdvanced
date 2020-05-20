from collections import deque

names_row = input()
names = deque(names_row.split(" "))
toss = int(input())

counter = 0
while True:
    if len(names) == 1:
        print(f'Last is {names.popleft()}')
        break
    counter += 1
    if counter < toss:
        names.append(names.popleft())
    elif counter == toss:
        print(f'Removed {names.popleft()}')
        counter = 0

