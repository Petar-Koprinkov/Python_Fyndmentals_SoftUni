command = input()
dictionary = {}

while command != "stop":
    count = int(input())

    if command not in dictionary.keys():
        dictionary[command] = 0
    dictionary[command] += count

    command = input()

for key, value in dictionary.items():
    print(f"{key} -> {value}")