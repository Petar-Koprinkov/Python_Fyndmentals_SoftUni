collection_of_items = input().split("|")
budget = float(input())
selling_list = []
profit = 0
train_ticket = 150

for items in collection_of_items:
    type_of_item, value_of_item = items.split("->")
    value_of_item = float(value_of_item)

    valid_value = False

    if type_of_item == "Clothes":
        if value_of_item <= 50.00:
            valid_value = True
    elif type_of_item == "Shoes":
        if value_of_item <= 35.00:
            valid_value = True
    elif type_of_item == "Accessories":
        if value_of_item <= 20.50:
            valid_value = True

    if valid_value:
        if value_of_item <= budget:
            budget -= value_of_item
            new_price = value_of_item * 1.40
            profit += new_price - value_of_item
            selling_list.append(new_price)

for price in selling_list:
    print(f"{price:.2f}", end=" ")
print()

print(f"Profit: {profit:.2f}")

total_income = budget + sum(selling_list)

if total_income >= train_ticket:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")