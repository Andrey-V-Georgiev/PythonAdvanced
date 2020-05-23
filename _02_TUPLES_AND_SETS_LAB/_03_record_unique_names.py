rows_count = int(input())
names_set = set()
for i in range(rows_count):
    names_set.add(input())
[print(n) for n in names_set]


