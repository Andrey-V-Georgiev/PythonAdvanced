def print_comb(str, index):

    if index >= len(str):
        print("".join(str))
        return

    print_comb(str, index + 1)

    for i in range(index + 1, len(str)):
        str[index], str[i] = str[i], str[index]
        print_comb(str, index + 1)
        str[index], str[i] = str[i], str[index]


str_input = list(input())
print_comb(str_input, 0)
