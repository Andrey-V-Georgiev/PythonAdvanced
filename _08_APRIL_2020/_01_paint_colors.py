main_colors = ['red', 'yellow', 'blue']
secondary_colors = {
    'orange': ('red', 'yellow'),
    'purple': ('red', 'blue'),
    'green': ('yellow', 'blue')
}
base_strings = input().split()
made_colors_all = []
made_colors_final = []

while base_strings:
    first_string = base_strings.pop(0)
    second_string = base_strings.pop() if base_strings else ""
    first_combination = (first_string + second_string)
    second_combination = (second_string + first_string)
    if first_combination in main_colors or first_combination in secondary_colors:
        made_colors_all.append(first_combination)
    elif second_combination in main_colors or second_combination in secondary_colors:
        made_colors_all.append(second_combination)
    else:
        if first_string[:-1] != '':
            base_strings.insert(len(base_strings) // 2, first_string[:-1])
        if second_string[:-1] != '':
            base_strings.insert(len(base_strings) // 2, second_string[:-1])

for color in made_colors_all:
    if color in secondary_colors:
        if secondary_colors[color][0] in made_colors_all and secondary_colors[color][1] in made_colors_all:
            made_colors_final.append(color)
    else:
        made_colors_final.append(color)

print(made_colors_final)
