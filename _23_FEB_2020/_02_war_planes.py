battlefield_size = int(input())
battlefield = []
plane_position = []
targets_count = [0]

for i in range(battlefield_size):
    row_list = list(input().split())
    battlefield.append(row_list)
    for j in range(battlefield_size):
        if row_list[j] == 'p':
            plane_position = [i, j]
        elif row_list[j] == 't':
            targets_count[0] += 1

initial_target_count = int(targets_count[0])
directions = {
    'up': (-1, 0),
    'right': (0, 1),
    'down': (1, 0),
    'left': (0, -1)
}


def shoot(_old_row, _old_col, _direction, _steps):
    if _direction == 'up':
        target_row, target_col = _old_row - _steps, _old_col
        if 0 <= target_row < battlefield_size and 0 <= target_col < battlefield_size:
            target_value = battlefield[target_row][target_col]
            if target_value == 't':
                targets_count[0] -= 1
            battlefield[target_row][target_col] = 'x'
    elif _direction == 'down':
        target_row, target_col = _old_row + _steps, _old_col
        if 0 <= target_row < battlefield_size and 0 <= target_col < battlefield_size:
            target_value = battlefield[target_row][target_col]
            if target_value == 't':
                targets_count[0] -= 1
            battlefield[target_row][target_col] = 'x'
    elif _direction == 'left':
        target_row, target_col = _old_row, _old_col - _steps
        if 0 <= target_row < battlefield_size and 0 <= target_col < battlefield_size:
            target_value = battlefield[target_row][target_col]
            if target_value == 't':
                targets_count[0] -= 1
            battlefield[target_row][target_col] = 'x'
    elif _direction == 'right':
        target_row, target_col = _old_row, _old_col + _steps
        if 0 <= target_row < battlefield_size and 0 <= target_col < battlefield_size:
            target_value = battlefield[target_row][target_col]
            if target_value == 't':
                targets_count[0] -= 1
            battlefield[target_row][target_col] = 'x'


def move(_old_row, _old_col, _direction, _steps):
    if _direction == 'up':
        target_row, target_col = _old_row - _steps, _old_col
        if 0 <= target_row < battlefield_size and 0 <= target_col < battlefield_size:
            target_value = battlefield[target_row][target_col]
            if target_value != '.':
                return
            battlefield[_old_row][_old_col] = '.'
            battlefield[target_row][target_col] = 'p'
            plane_position[0], plane_position[1] = target_row, target_col
        else:
            return
    elif _direction == 'down':
        target_row, target_col = _old_row + _steps, _old_col
        if 0 <= target_row < battlefield_size and 0 <= target_col < battlefield_size:
            target_value = battlefield[target_row][target_col]
            if target_value != '.':
                return
            battlefield[_old_row][_old_col] = '.'
            battlefield[target_row][target_col] = 'p'
            plane_position[0], plane_position[1] = target_row, target_col
        else:
            return
    elif _direction == 'left':
        target_row, target_col = _old_row, _old_col - _steps
        if 0 <= target_row < battlefield_size and 0 <= target_col < battlefield_size:
            target_value = battlefield[target_row][target_col]
            if target_value != '.':
                return
            battlefield[_old_row][_old_col] = '.'
            battlefield[target_row][target_col] = 'p'
            plane_position[0], plane_position[1] = target_row, target_col
        else:
            return
    elif _direction == 'right':
        target_row, target_col = _old_row, _old_col + _steps
        if 0 <= target_row < battlefield_size and 0 <= target_col < battlefield_size:
            target_value = battlefield[target_row][target_col]
            if target_value != '.':
                return
            battlefield[_old_row][_old_col] = '.'
            battlefield[target_row][target_col] = 'p'
            plane_position[0], plane_position[1] = target_row, target_col
        else:
            return


def print_battlefield():
    for row in battlefield:
        str_row = ' '.join(row)
        print(str_row)


def print_accomplished():
    print(f'Mission accomplished! All {initial_target_count} targets destroyed.')
    print_battlefield()


commands_size = int(input())
for k in range(commands_size):
    command_list = input().split()
    command, direction, steps = command_list[0], command_list[1], int(command_list[2])
    direction_change = directions[direction]
    old_row, old_col = plane_position[0], plane_position[1]
    if command == 'shoot':
        shoot(old_row, old_col, direction, steps)
        if targets_count[0] == 0:
            print_accomplished()
            break
    elif command == 'move':
        move(old_row, old_col, direction, steps)
        pass

if targets_count[0] > 0:
    print(f'Mission failed! {targets_count[0]} targets left.')
    print_battlefield()
