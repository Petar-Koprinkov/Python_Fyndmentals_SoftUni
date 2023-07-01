number = int(input())
dictionary = {}

for _ in range(number):
    word = input()
    synonym = input()

    if word not in dictionary.keys():
        dictionary[word] = []
    dictionary[word].append(synonym)

for key, value in dictionary.items():
    print(f"{key} - {', '.join(value)}")

