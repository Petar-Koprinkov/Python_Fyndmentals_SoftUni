lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
gladiator_expenses = 0

for game in range(1, lost_fight_count + 1):
    if game % 2 == 0:
        gladiator_expenses += helmet_price
    if game % 3 == 0:
        gladiator_expenses += sword_price
    if game % 6 == 0:
        gladiator_expenses += shield_price
    if game % 12 == 0:
        gladiator_expenses += armor_price

print(f"Gladiator expenses: {gladiator_expenses:.2f} aureus")





