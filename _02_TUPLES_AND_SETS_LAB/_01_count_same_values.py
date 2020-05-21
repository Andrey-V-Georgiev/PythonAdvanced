def include(dictionary, val):
    for k in dictionary.keys():
        if k == val:
            return True

    return False


arr = input().split(" ")
num_arr = [float(i) for i in arr]
data_dictionary = {}

for i in range(len(num_arr)):
    if include(data_dictionary, num_arr[i]):
        data_dictionary[num_arr[i]] += 1
    else:
        data_dictionary[num_arr[i]] = 1

for key, value in data_dictionary.items():
    print(f'{key} - {value} times')
