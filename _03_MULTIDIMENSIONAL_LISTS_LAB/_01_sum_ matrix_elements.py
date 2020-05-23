rows, cols = map(int, input().split(', '))
m_list = []
total_sum = 0
for r in range(rows):
    m_list.append(list(map(int, input().split(', '))))
for r in range(rows):
    for c in range(cols):
        total_sum += m_list[r][c]
print(total_sum)
print(m_list)
