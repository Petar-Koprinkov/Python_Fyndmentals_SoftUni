single_line = input().lower().split()
dictionary = {}

for element in single_line:
    if element not in dictionary.keys():
        dictionary[element] = 0
    dictionary[element] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")