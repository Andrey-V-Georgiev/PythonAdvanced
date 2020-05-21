def contains(dict_keys, key):
    for k in dict_keys:
        if k == key:
            return True
    return False


number_of_rows = int(input())
input_strings = list()
name_keys = set()
data_dict = dict()

for i in range(number_of_rows):
    input_strings.append(input())

for str_row in input_strings:
    name, grade = str_row.split(" ")
    if contains(data_dict.keys(), name):
        data_dict[name].append(float(grade))
    else:
        data_dict[name] = [float(grade)]

for s_name, s_grades in data_dict.items():
    avg_grade = sum(s_grades) / len(s_grades)
    grades_str = ' '.join(f'{g:.2f}' for g in s_grades)
    print(f'{s_name} -> {grades_str} (avg: {avg_grade:.2f})')


