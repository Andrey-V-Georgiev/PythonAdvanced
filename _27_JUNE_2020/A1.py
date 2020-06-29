from collections import deque

effects = deque(map(int, input().split(', ')))
casings = deque(map(int, input().split(', ')))

mix_table = dict({
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs'
})
count_crafted = dict({
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
})

while effects and casings:

    first_num = effects.popleft()
    second_num = casings.pop()
    current_sum = first_num + second_num

    if current_sum in mix_table.keys():
        bomb_name = mix_table[current_sum]
        count_crafted[bomb_name] += 1
        success = (count_crafted['Datura Bombs'] >= 3 and count_crafted['Cherry Bombs'] >= 3 and count_crafted[
            'Smoke Decoy Bombs'] >= 3)
        if success:
            break
    else:
        second_num -= 5
        effects.appendleft(first_num)
        casings.append(second_num)

success = (count_crafted['Datura Bombs'] >= 3 and count_crafted['Cherry Bombs'] >= 3 and count_crafted[
    'Smoke Decoy Bombs'] >= 3)
# print first section
if success:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

# print second section
if effects:
    bomb_effects = ', '.join(map(str, effects))
    print(f'Bomb Effects: {bomb_effects}')
else:
    print('Bomb Effects: empty')

if casings:
    bomb_casings = ', '.join(map(str, casings))
    print(f'Bomb Casings: {bomb_casings}')
else:
    print('Bomb Casings: empty')

# print third section
for key, value in sorted(count_crafted.items()):
    print(f'{key}: {value}')
