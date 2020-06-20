from collections import deque

main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']
all_colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']
mix_table = {
    'orange': ('red', 'yellow'),
    'purple': ('red', 'blue'),
    'green': ('yellow', 'blue')
}
my_colors = []


def find_middle_index():
    list_length = len(input_deque)
    _mid_index = list_length / 2
    return round(_mid_index)


def filter_secondary_colors():
    _my_final_colors = []
    _sc_resource = [c for c in my_colors if c in main_colors]
    for c in my_colors:
        if c in main_colors and c not in secondary_colors:
            _my_final_colors.append(c)
        elif c in secondary_colors and c not in main_colors:
            needed_combination = mix_table[c]
            if needed_combination[0] in _sc_resource and needed_combination[1] in _sc_resource:
                _my_final_colors.append(c)
    return _my_final_colors


input_deque = deque(input().split())
while input_deque:
    left_word = input_deque.popleft()
    right_word = input_deque.pop() if len(input_deque) > 0 else None
    if left_word in all_colors:
        my_colors.append(left_word)
        continue
    if right_word:
        if (left_word + right_word) in all_colors:
            my_colors.append(left_word + right_word)
        elif (right_word + left_word) in all_colors:
            my_colors.append(right_word + left_word)
        else:
            if len(input_deque) == 0:
                break
            left_word = left_word[:-1] if len(left_word) > 0 else None
            right_word = right_word[:-1] if len(right_word) > 0 else None
            concat_word = None
            if left_word and right_word:
                concat_word = left_word + right_word
            elif left_word:
                concat_word = left_word
            elif right_word:
                concat_word = right_word
            mid_index = find_middle_index()
            input_deque.insert(mid_index, concat_word)

my_final_colors = filter_secondary_colors()
print(my_final_colors)
