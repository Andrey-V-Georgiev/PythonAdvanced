n = int(input())
m_list = [input() for _ in range(n)]
sym = input()
have_appearance = False
for r in range(n):
    for c in range(n):
        if m_list[r][c] == sym:
            have_appearance = True
            print(f'({r}, {c})')
            break
    if have_appearance:
        break
if not have_appearance:
    print(f'{sym} does not occur in the matrix')
