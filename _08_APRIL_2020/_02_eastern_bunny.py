import sys

size = int(input())
matrix = []
player_position = []
# Fill up the matrix and find player position
for i in range(size):
    row_list = list(input().split())
    matrix.append(row_list)
    for j in range(size):
        if row_list[j] == 'B':
            player_position = [i, j]

player_row, player_col = player_position[0], player_position[1]
biggest_sum = -sys.maxsize - 1
biggest_sum_key = ''

# check up
up_positions = []
up_sum = 0
for i_up in range(player_row - 1, 0, -1):
    val_up = matrix[i_up][player_col]
    if val_up == 'X':
        break
    else:
        up_sum += int(val_up)
        up_positions.append([i_up, player_col])
if biggest_sum < up_sum and len(up_positions) > 0:
    biggest_sum = up_sum
    biggest_sum_key = 'up_positions'

# check down
down_positions = []
down_sum = 0
for i_down in range(player_row + 1, size):
    val_down = matrix[i_down][player_col]
    if val_down == 'X':
        break
    else:
        down_sum += int(val_down)
        down_positions.append([i_down, player_col])
if biggest_sum < down_sum and len(down_positions) > 0:
    biggest_sum = down_sum
    biggest_sum_key = 'down_positions'

# check left
left_positions = []
left_sum = 0
for i_left in range(player_col - 1, 0, -1):
    val_left = matrix[player_row][i_left]
    if val_left == 'X':
        break
    else:
        left_sum += int(val_left)
        left_positions.append([player_row, i_left])
if biggest_sum < left_sum and len(left_positions) > 0:
    biggest_sum = left_sum
    biggest_sum_key = 'left_positions'

# check right
right_positions = []
right_sum = 0
for i_right in range(player_col + 1, size):
    val_right = matrix[player_row][i_right]
    if val_right == 'X':
        break
    else:
        right_sum += int(val_right)
        right_positions.append([player_row, i_right])
if biggest_sum < right_sum and len(right_positions) > 0:
    biggest_sum = right_sum
    biggest_sum_key = 'right_positions'

if biggest_sum_key == 'up_positions':
    print('up')
    [print(position) for position in up_positions]
    print(up_sum)
elif biggest_sum_key == 'down_positions':
    print('down')
    [print(position) for position in down_positions]
    print(down_sum)
elif biggest_sum_key == 'left_positions':
    print('left')
    [print(position) for position in left_positions]
    print(left_sum)
elif biggest_sum_key == 'right_positions':
    print('right')
    [print(position) for position in right_positions]
    print(right_sum)

