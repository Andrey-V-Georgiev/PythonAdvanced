from collections import deque

# first line input
crafting_materials_int_list = [int(cm) for cm in input().strip().split()]
crafting_materials = deque(crafting_materials_int_list)
# second line input
magic_levels_int_list = [int(ml) for ml in input().strip().split()]
magic_levels = deque(magic_levels_int_list)
# hardcoded values
mix_table = dict({150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'})
crafted_presents = dict({'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0})

# stop crafting presents when you run out of boxes of materials or magic level values
while len(crafting_materials) > 0 and len(magic_levels) > 0:

    last_material = crafting_materials.pop()
    first_magic = magic_levels.popleft()
    total_magic_level = last_material * first_magic

    # if the result equals one of the levels described in the table above
    # craft the present and remove both materials and magic value
    if total_magic_level in mix_table.keys():
        present_name = mix_table[total_magic_level]
        crafted_presents[present_name] += 1
    else:
        # if the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents
        if (last_material == 0 and first_magic == 0):
            pass
        elif last_material == 0 or first_magic == 0:
            if last_material == 0:
                magic_levels.appendleft(first_magic)
            if first_magic == 0:
                crafting_materials.append(last_material)

        # if the product doesn't equal one of the magic levels in the table and is a positive number,
        # remove only the magic value and increase the material value with 15
        elif total_magic_level > 0 and total_magic_level not in mix_table.keys():
            increased_material_value = last_material + 15
            crafting_materials.append(increased_material_value)

        # if the product of the operation is a negative number, then you have to sum the values together
        # remove them both from their positions and the result should be added to the materials
        elif total_magic_level < 0:
            sum_crafting_and_magic = last_material + first_magic
            crafting_materials.append(sum_crafting_and_magic)


def check_are_presents_crafted(crafted_presents):
    if crafted_presents['Doll'] > 0 and crafted_presents['Wooden train'] > 0:
        return True
    if crafted_presents['Teddy bear'] > 0 and crafted_presents['Bicycle'] > 0:
        return True
    return False


are_presents_crafted = check_are_presents_crafted(crafted_presents)

# on the first line - print whether you've succeeded in crafting the presents
if are_presents_crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

# on the next two lines print the materials and magic that are left, if there are any, otherwise skip the line
if len(crafting_materials) > 0:
    crafting_materials.reverse()
    material_string = ', '.join(map(str, crafting_materials))
    print(f'Materials left: {material_string}')

if len(magic_levels) > 0:
    magic_levels.reverse()
    magic_string = ', '.join(map(str, magic_levels))
    print(f'Magic left: {magic_string}')

# on the next lines print the presents you have crafted at least once, ordered alphabetically
sorted_presents = {key: value for key, value in sorted(crafted_presents.items(), key=lambda item: item[0])}
[print(f'{key}: {value}') for key, value in sorted_presents.items() if value > 0]
