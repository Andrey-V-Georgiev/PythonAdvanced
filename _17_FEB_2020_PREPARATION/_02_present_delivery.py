directions = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1)
}

santa_position = []
nice_kids_count = 0
count_presents = int(input())
nice_kids_given_presents = 0
size_matrix = int(input())


def print_when_not_enough_presents(_nice_kids_with_given_present):
    nice_kids_left = nice_kids_count - _nice_kids_with_given_present
    print('Santa ran out of presents!')
    for current_row in neighborhood:
        print(' '.join(current_row))
    print(f'No presents for {nice_kids_left} nice kid/s.')
    return


def print_when_enough_presents(_nice_kids_with_given_present):
    for current_row in neighborhood:
        print(' '.join(current_row))
    print(f'Good job, Santa! {_nice_kids_with_given_present} happy nice kid/s.')
    return


def give_cookie_presents(_santa_position, _next_santa_position, _count_presents, _nice_kids_given_presents):
    neighborhood[_santa_position[0]][_santa_position[1]] = '-'
    neighborhood[_next_santa_position[0]][_next_santa_position[1]] = 'S'

    r = _next_santa_position[0]
    c = _next_santa_position[1]

    value_up = neighborhood[r + directions['up'][0]][c + directions['up'][1]]
    neighborhood[r + directions['up'][0]][c + directions['up'][1]] = '-'
    value_right = neighborhood[r + directions['right'][0]][c + directions['right'][1]]
    neighborhood[r + directions['right'][0]][c + directions['right'][1]] = '-'
    value_down = neighborhood[r + directions['down'][0]][c + directions['down'][1]]
    neighborhood[r + directions['down'][0]][c + directions['down'][1]] = '-'
    value_left = neighborhood[r + directions['left'][0]][c + directions['left'][1]]
    neighborhood[r + directions['left'][0]][c + directions['left'][1]] = '-'

    position_values = [value_up, value_right, value_down, value_left]
    for value in position_values:
        if value in 'X':
            _count_presents -= 1
        if value in 'V':
            _nice_kids_given_presents += 1
            _count_presents -= 1
    return [_next_santa_position, _count_presents, _nice_kids_given_presents]


def give_presents(_santa_position, _next_santa_position, _count_presents, _nice_kids_given_presents):
    position_value = neighborhood[_next_santa_position[0]][_next_santa_position[1]]
    neighborhood[_santa_position[0]][_santa_position[1]] = '-'
    neighborhood[_next_santa_position[0]][_next_santa_position[1]] = 'S'
    if position_value in 'XV':
        if position_value in 'X':
            _count_presents -= 1
        if position_value in 'V':
            _nice_kids_given_presents += 1
            _count_presents -= 1
    return [_next_santa_position, _count_presents, _nice_kids_given_presents]


def find_next_santa_position(_direction, _santa_position):
    old_santa_row, old_santa_col = _santa_position[0], _santa_position[1]
    direction_row, direction_col = _direction[0], _direction[1]
    _next_santa_position = [(old_santa_row + direction_row), (old_santa_col + direction_col)]
    return _next_santa_position


neighborhood = list()
for row in range(size_matrix):
    neighborhood_row = list(input().split())
    neighborhood.append(neighborhood_row)

for row in range(size_matrix):
    for col in range(size_matrix):
        current_cell = neighborhood[row][col]
        if current_cell == 'S':
            santa_position = [row, col]
        elif current_cell == 'V':
            nice_kids_count += 1

command = input()
global next_santa_position
while command != 'Christmas morning' and count_presents:

    if command == 'up':
        next_santa_position = find_next_santa_position(directions['up'], santa_position)
    elif command == 'right':
        next_santa_position = find_next_santa_position(directions['right'], santa_position)
    elif command == 'down':
        next_santa_position = find_next_santa_position(directions['down'], santa_position)
    elif command == 'left':
        next_santa_position = find_next_santa_position(directions['left'], santa_position)
    if neighborhood[next_santa_position[0]][next_santa_position[1]] == 'C':
        santa_position, count_presents, nice_kids_given_presents = give_cookie_presents(
            santa_position, next_santa_position, count_presents, nice_kids_given_presents
        )
    else:
        santa_position, count_presents, nice_kids_given_presents = give_presents(
            santa_position, next_santa_position, count_presents, nice_kids_given_presents
        )
    if count_presents == 0:
        break
    command = input()

if count_presents == 0 and nice_kids_count > nice_kids_given_presents:
    print_when_not_enough_presents(nice_kids_given_presents)
else:
    print_when_enough_presents(nice_kids_given_presents)
