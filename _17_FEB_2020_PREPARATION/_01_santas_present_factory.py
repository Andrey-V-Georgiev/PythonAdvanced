from collections import deque

materials = list(map(int, input().strip().split()))
magics = deque(map(int, input().strip().split()))

mix_table = dict({150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'})
crafted_presents = dict({'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0})

while materials and magics:

    current_material = materials.pop()
    current_magic = magics.popleft()
    total_magic = current_material * current_magic

    if total_magic in mix_table.keys():
        present_name = mix_table[total_magic]
        crafted_presents[present_name] += 1
    else:
        if total_magic < 0:
            materials.append(current_material + current_magic)
        elif total_magic > 0:
            increased_material_value = current_material + 15
            materials.append(increased_material_value)
        else:
            if current_material:
                materials.append(current_material)
            if current_magic:
                magics.appendleft(current_magic)

success = (crafted_presents['Doll'] and crafted_presents['Wooden train']) or \
          (crafted_presents['Teddy bear'] and crafted_presents['Bicycle'])
# print first section
if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

# print second section
if materials:
    materials_string = ', '.join(map(str, reversed(materials)))
    print(f'Materials left: {materials_string}')
if magics:
    magics_string = ', '.join(map(str, magics))
    print(f'Magic left: {magics_string}')

# print third section
for key, value in sorted(crafted_presents.items()):
    if value:
        print(f'{key}: {value}')
