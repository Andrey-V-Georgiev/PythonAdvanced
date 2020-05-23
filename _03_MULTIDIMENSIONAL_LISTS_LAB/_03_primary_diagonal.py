n = int(input())
m_list = [list(map(int, input().split(' '))) for _ in range(n)]
pd_sum = 0
for i in range(n):
    pd_sum += m_list[i][i]
print(pd_sum)
