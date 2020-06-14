def get_magic_triangle(n):
    triangle_list = [[1], [1, 1]]
    for i in range(1, n - 1):
        current_row = triangle_list[i]
        next_row = list()
        for j in range(len(current_row) - 1):
            next_row.append(current_row[j] + current_row[j + 1])
        next_row.insert(0, 1)
        next_row.append(1)
        triangle_list.append(next_row)
    return triangle_list


print(get_magic_triangle(5))


