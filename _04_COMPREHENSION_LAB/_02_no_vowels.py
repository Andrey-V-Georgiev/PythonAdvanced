vowels = ['a', 'o', 'u', 'e', 'i']
input_str = input()
output_result = ''.join([ch for ch in input_str if ch.lower() not in vowels])
print(output_result)
