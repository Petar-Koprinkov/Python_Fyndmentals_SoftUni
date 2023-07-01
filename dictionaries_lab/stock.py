products = input().split()
dictionary = {}

for index in range(0, len(products), 2):
    key = products[index]
    value = int(products[index + 1])
    dictionary[key] = value

searched_products = input().split()

for product in searched_products:
    if product in dictionary:
        print(f"We have {dictionary[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")