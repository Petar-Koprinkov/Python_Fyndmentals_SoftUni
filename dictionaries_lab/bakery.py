products = input().split()
dictionary = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = int(products[index + 1])
    dictionary[key] = value

print(dictionary)

