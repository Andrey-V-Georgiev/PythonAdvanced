import sys


def sum_sub_matrix(m, r, c):
    return m[r][c] + m[r][c + 1] + m[r + 1][c] + m[r + 1][c + 1]


rows, cols = map(int, input().split(', '))
m_list = [list(map(int, input().split(', '))) for _ in range(rows)]
max_sum = -sys.maxsize - 1
max_r = 0
max_c = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        current_sub_sum = sum_sub_matrix(m_list, row, col)
        if current_sub_sum > max_sum:
            max_r = row
            max_c = col
            max_sum = current_sub_sum

print(f'{m_list[max_r][max_c]} {m_list[max_r][max_c + 1]}')
print(f'{m_list[max_r + 1][max_c]} {m_list[max_r + 1][max_c + 1]}')
print(max_sum)
