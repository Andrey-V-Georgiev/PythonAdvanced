def parse_to_list(str_row):
    return list(map(int, str_row.split(', ')))


n = int(input())
matrix = [parse_to_list(input()) for i in range(n)]
output_list = [col for row in matrix for col in row]
print(output_list)
