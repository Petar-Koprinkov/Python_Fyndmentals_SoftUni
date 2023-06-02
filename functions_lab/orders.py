def restaurant(orders, quantity):
    price = 0

    if orders == "coffee":
        price = 1.50 * quantity
    elif orders == "coke":
        price = 1.40 * quantity
    elif orders == "water":
        price = 1 * quantity
    elif orders == "snacks":
        price = 2 * quantity

    return f"{price:.2f}"


product = input()
counter = int(input())

print(restaurant(product, counter))



