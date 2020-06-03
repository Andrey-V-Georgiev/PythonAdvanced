from collections import deque

# directions
move_up = (-1, 0)
move_down = (1, 0)
move_left = (0, -1)
move_right = (0, 1)

santa_position = []
naughty_kids_count = 0
nice_kids_count = 0

# dimensions input data
count_of_presents = int(input())
size_of_matrix = int(input())

# receive the matrix
matrix = list()
for row in range(size_of_matrix):
    row_input_list = list(input().split())
    matrix.append(row_input_list)
    for col in range(size_of_matrix):
        current_cell = row_input_list[col]
        if current_cell == 'S':
            santa_position = [row, col]
        elif current_cell == 'X':
            naughty_kids_count += 1
        elif current_cell == 'V':
            nice_kids_count += 1

# receive the commands
commands_deque = deque()
command = input()
while command != 'Christmas morning':
    commands_deque.append(command)
    command = input()


def change_santa_position(santa_position_arg, direction):
    new_santa_row = santa_position_arg[0] + direction[0]
    new_santa_col = santa_position_arg[1] + direction[0]
    return [new_santa_row, new_santa_col]


def give_cookie_presents(position_coordinates, matrix_arg, count_of_presents_arg):
    row = position_coordinates[0]
    col = position_coordinates[1]
    position_type = matrix_arg[row][col]
    if position_type == 'X':
        count_of_presents_arg -= 1
        matrix_arg[row][col] = '-'
        return [matrix_arg, count_of_presents_arg]
    elif position_type == 'V':
        count_of_presents_arg -= 1
        matrix_arg[row][col] = '-'
        return [matrix_arg, count_of_presents_arg]
    else:
        matrix_arg[row][col] = '-'
        return [matrix_arg, count_of_presents_arg]


def do_cookie_mood(santa_position_arg, matrix_arg, count_of_presents_arg):
    position_up_coordinates = change_santa_position(santa_position_arg, move_up)
    matrix_arg, count_of_presents_arg = give_cookie_presents(
        position_up_coordinates, matrix_arg, count_of_presents_arg
    )
    if len(count_of_presents_arg) == 0:
        return [santa_position_arg, matrix_arg, count_of_presents_arg]
    position_down_coordinates = change_santa_position(santa_position_arg, move_down)
    matrix_arg, count_of_presents_arg = give_cookie_presents(
        position_down_coordinates, matrix_arg, count_of_presents_arg
    )
    if len(count_of_presents_arg) == 0:
        return [santa_position_arg, matrix_arg, count_of_presents_arg]
    position_left_coordinates = change_santa_position(santa_position_arg, move_left)
    matrix_arg, count_of_presents_arg = give_cookie_presents(
        position_left_coordinates, matrix_arg, count_of_presents_arg
    )
    if len(count_of_presents_arg) == 0:
        return [santa_position_arg, matrix_arg, count_of_presents_arg]
    position_right_coordinates = change_santa_position(santa_position_arg, move_right)
    matrix_arg, count_of_presents_arg = give_cookie_presents(
        position_right_coordinates, matrix_arg, count_of_presents_arg
    )
    return [santa_position_arg, matrix_arg, count_of_presents_arg]


def give_presents(santa_position_arg, matrix_arg, count_of_presents_arg):
    santa_row = santa_position_arg[0]
    santa_col = santa_position_arg[1]
    position_type = matrix_arg[santa_row][santa_col]
    if position_type == '-':
        return [matrix_arg, count_of_presents_arg]
    elif position_type == 'X':
        matrix_arg[santa_row][santa_col] = '-'
        return [matrix_arg, count_of_presents_arg]
    elif position_type == 'V':
        matrix_arg[santa_row][santa_col] = '-'
        count_of_presents_arg -= 1
        return [matrix_arg, count_of_presents_arg]
    elif position_type == 'C':
        do_cookie_mood(santa_position_arg, matrix_arg, count_of_presents_arg)
        return [matrix_arg, count_of_presents_arg]


def print_output(matrix_arg, nice_kids_count_arg):
    pass


while len(commands_deque) > 0:
    current_command = commands_deque.popleft()
    if current_command == 'up':
        santa_position = change_santa_position(santa_position, move_up)
        matrix, count_of_presents = give_presents(santa_position, matrix, count_of_presents)
        if len(count_of_presents) == 0:
            print_output(matrix, nice_kids_count)
    elif current_command == 'down':
        santa_position = change_santa_position(santa_position, move_down)
        matrix, count_of_presents = give_presents(santa_position, matrix, count_of_presents)
    elif current_command == 'left':
        santa_position = change_santa_position(santa_position, move_left)
        matrix, count_of_presents = give_presents(santa_position, matrix, count_of_presents)
    elif current_command == 'right':
        santa_position = change_santa_position(santa_position, move_right)
        matrix, count_of_presents = give_presents(santa_position, matrix, count_of_presents)
