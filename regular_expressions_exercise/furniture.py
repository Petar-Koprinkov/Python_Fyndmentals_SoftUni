import re

text = input()
bought_items = []
total_price = 0

while text != "Purchase":

    pattern = r">>\b(?P<furniture>[a-zA-Z]+)<<(?P<price>\d+\.?\d+)!(?P<quantity>\d*)\b"

    matches = re.search(pattern, text)

    if matches:
        furniture, price, quantity = matches.groups()
        bought_items.append(furniture)
        total_price += float(price)*int(quantity)

    text = input()

print("Bought furniture:")
for item in bought_items:
    print(item)
print(f"Total money spend: {total_price:.2f}")