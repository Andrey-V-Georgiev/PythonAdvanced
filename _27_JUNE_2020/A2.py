territory_size = int(input())
territory = list()
current_row, current_col = 0, 0
next_row, next_col = 0, 0
burrow_positions = list()

for i in range(territory_size):
    row_list = input()
    territory.append(list(row_list))
    for j in range(territory_size):
        if row_list[j] == 'S':
            current_row, current_col = i, j
        elif row_list[j] == 'B':
            burrow_positions.append((i, j))

directions = {
    'up': (-1, 0),
    'right': (0, 1),
    'down': (1, 0),
    'left': (0, -1)
}

food_quantity = 0
while True:
    command = input() or ''
    if command == '':
        break
    try:
        if command == 'up':
            next_row, next_col = int(current_row + directions['up'][0]), int(current_col + directions['up'][1])
        elif command == 'down':
            next_row, next_col = int(current_row + directions['down'][0]), int(current_col + directions['down'][1])
        elif command == 'left':
            next_row, next_col = int(current_row + directions['left'][0]), int(current_col + directions['left'][1])
        elif command == 'right':
            next_row, next_col = int(current_row + directions['right'][0]), int(current_col + directions['right'][1])
        if next_row < 0 or next_col < 0:
            territory[current_row][current_col] = '.'
            break
        next_pos_value = territory[next_row][next_col]
        if next_pos_value == '-':
            territory[current_row][current_col] = '.'
            territory[next_row][next_col] = 'S'
            current_row, current_col = next_row, next_col
        elif next_pos_value == '*':
            territory[current_row][current_col] = '.'
            territory[next_row][next_col] = 'S'
            current_row, current_col = next_row, next_col
            food_quantity += 1
            if food_quantity == 10:
                break
        elif next_pos_value == 'B':
            b_row_1 = burrow_positions[0][0]
            b_col_1 = burrow_positions[0][1]
            b_row_2 = burrow_positions[1][0]
            b_col_2 = burrow_positions[1][1]

            if next_row == b_row_1 and next_col == b_col_1:
                territory[current_row][current_col] = '.'
                territory[next_row][next_col] = '.'
                territory[burrow_positions[1][0]][burrow_positions[1][1]] = 'S'
                current_row, current_col = burrow_positions[1][0], burrow_positions[1][1]
            elif next_row == b_row_2 and next_col == b_col_2:
                territory[current_row][current_col] = '.'
                territory[next_row][next_col] = '.'
                territory[burrow_positions[0][0]][burrow_positions[0][1]] = 'S'
                current_row, current_col = burrow_positions[0][0], burrow_positions[0][1]

    except:
        territory[current_row][current_col] = '.'
        break

if food_quantity == 10:
    print('You won! You fed the snake.')
else:
    print('Game over!')

print(f'Food eaten: {food_quantity}')

for i in range(territory_size):
    row_str = ''.join(territory[i])
    print(row_str)
