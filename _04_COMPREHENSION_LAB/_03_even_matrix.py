def parse_to_dict(input_row):
    return list(map(int, input_row.split(', ')))


rows_count = int(input())
initial_matrix = [parse_to_dict(input()) for i in range(rows_count)]
even_matrix = [[num for num in row if num % 2 == 0] for row in initial_matrix]
print(even_matrix)
