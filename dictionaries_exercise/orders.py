dictionary = {}
products = input()

while products != "buy":
    products = products.split()
    name = products[0]
    price = float(products[1])
    quantity = int(products[2])

    if name not in dictionary.keys():
        dictionary[name] = [0, 0]
    dictionary[name][0] += quantity
    dictionary[name][1] = price

    products = input()

for key, value in dictionary.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")