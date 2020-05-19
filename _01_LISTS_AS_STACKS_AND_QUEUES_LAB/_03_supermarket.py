from collections import deque

names = deque()

while True:
    row = input()
    if row == "Paid":
        while len(names):
            print(names.popleft())
    elif row == "End":
        print(f"{len(names)} people remaining.")
        break
    else:
        names.append(row)


