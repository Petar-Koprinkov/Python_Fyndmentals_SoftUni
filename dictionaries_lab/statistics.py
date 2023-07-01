dictionary = {}

while True:
    command = input()
    if command == "statistics":
        break

    command = command.split(": ")

    product = command[0]
    quantity = int(command[1])

    if product not in dictionary.keys():
        dictionary[product] = 0
    dictionary[product] += quantity

total_products = len(dictionary)
total_quantity = sum(dictionary.values())

print("Products in stock:")

for key, value in dictionary.items():
    print(f"- {key}: {value}")

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")




