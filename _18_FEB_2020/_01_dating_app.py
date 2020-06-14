from collections import deque


def is_divisible(_num):
    return _num % 25 == 0


males = list(map(int, input().split()))
females = deque(map(int, input().split()))
successful_matches = 0

while males and females:

    current_male = males.pop()
    current_female = females.popleft()

    if current_male <= 0 or current_female <= 0:
        if current_male <= 0:
            females.appendleft(current_female)
        if current_female <= 0:
            males.append(current_male)
    elif is_divisible(current_female) or is_divisible(current_male):
        if is_divisible(current_male):
            if males:
                males.pop()
            females.appendleft(current_female)
        if is_divisible(current_female):
            if females:
                females.popleft()
            males.append(current_male)
    elif current_male == current_female:
        successful_matches += 1
    elif current_male != current_female:
        decreased_male = current_male - 2
        males.append(decreased_male)

print(f'Matches: {successful_matches}')
if males:
    males_string = ', '.join(map(str, reversed(males)))
    print(f'Males left: {males_string}')
else:
    print('Males left: none')

if females:
    females_string = ', '.join(map(str, females))
    print(f'Females left: {females_string}')
else:
    print('Females left: none')
