number_of_city = int(input())
total_profit = 0

for city in range(1, number_of_city + 1):
    name_of_city = input()
    money_earned = float(input())
    money_earned_expenses = float(input())

    if city % 5 == 0:
        money_earned = money_earned - (money_earned * 0.10)
    elif city % 3 == 0:
        money_earned_expenses *= 1.50

    profit = money_earned - money_earned_expenses

    total_profit += profit

    print(f"In {name_of_city} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")

