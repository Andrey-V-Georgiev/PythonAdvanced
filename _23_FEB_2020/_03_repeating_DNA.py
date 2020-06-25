def get_repeating_DNA(full_string):
    occurrences_list = []
    for i in range(0, len(full_string) - 10):
        tmp_substring = full_string[i:i + 10]
        tmp_full_string = full_string[i + 1:]
        if tmp_substring in tmp_full_string:
            occurrences_list.append(tmp_substring)
    return occurrences_list


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)
