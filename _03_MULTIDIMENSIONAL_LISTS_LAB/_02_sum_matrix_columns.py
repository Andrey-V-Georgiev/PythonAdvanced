rows, cols = map(int, input().split(', '))
m_list = [list(map(int, input().split(' '))) for _ in range(rows)]
for c in range(cols):
    col_sum = 0
    for r in range(rows):
        col_sum += m_list[r][c]
    print(col_sum)


