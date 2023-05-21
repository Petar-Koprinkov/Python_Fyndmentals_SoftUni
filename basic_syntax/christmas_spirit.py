quantity_of_decoration = int(input())
days_left = int(input())

ORNAMENT_SET_PRICE = 2
TREE_SKIRT_PRICE = 5
TREE_GARLAND_PRICE = 3
TREE_LIGHTS_PRICE = 15

total_cost = 0
total_spirit = 0

for days in range(1, days_left + 1):
    if days % 11 == 0:
        quantity_of_decoration += 2
    if days % 2 == 0:
        total_cost += ORNAMENT_SET_PRICE * quantity_of_decoration
        total_spirit += 5
    if days % 3 == 0:
        total_cost += (TREE_SKIRT_PRICE + TREE_GARLAND_PRICE) * quantity_of_decoration
        total_spirit += 13
    if days % 5 == 0:
        total_cost += TREE_LIGHTS_PRICE * quantity_of_decoration
        total_spirit += 17
        if days % 3 == 0:
            total_spirit += 30
    if days % 10 == 0:
        total_spirit -= 20
        total_cost += TREE_SKIRT_PRICE + TREE_GARLAND_PRICE + TREE_LIGHTS_PRICE

if days_left % 10 ==0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
