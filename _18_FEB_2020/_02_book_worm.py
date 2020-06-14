text_list = list(input())
length_matrix = int(input())
matrix = []
player_position = []
for i in range(length_matrix):
    row = list(input())
    matrix.append(row)
    for j in range(length_matrix):
        if row[j] == 'P':
            player_position = [i, j]
directions = {
    'up': (-1, 0),
    'right': (0, 1),
    'down': (1, 0),
    'left': (0, -1)
}

length_commands = int(input())
for k in range(length_commands):

    command = input()
    direction_change = directions[command]
    old_row, old_col = player_position[0], player_position[1]
    next_row, next_col = old_row + direction_change[0], old_col + direction_change[1]

    if 0 <= next_row < length_matrix and 0 <= next_col < length_matrix:
        next_position_value = matrix[next_row][next_col]
        if next_position_value != '-':
            text_list.append(next_position_value)
        matrix[player_position[0]][player_position[1]], matrix[next_row][next_col] = '-', 'P'
        player_position = [next_row, next_col]
    else:
        if text_list:
            text_list.pop()

print(''.join(text_list))
for row in matrix:
    print(''.join(row))
