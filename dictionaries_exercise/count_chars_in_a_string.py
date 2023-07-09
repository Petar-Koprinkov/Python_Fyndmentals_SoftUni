message = [letter for letter in input() if letter != " "]
dictionary = {}

for char in message:
    if char not in dictionary.keys():
        dictionary[char] = 0
    dictionary[char] += 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")