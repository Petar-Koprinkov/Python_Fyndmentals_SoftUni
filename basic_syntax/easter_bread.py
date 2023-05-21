budget = float(input())
price_for_1_kg_flour = float(input())
price_for_1_pack_of_egg = 0.75 * price_for_1_kg_flour
price_for_1L_milk = 1.25 * price_for_1_kg_flour
colored_eggs = 0
current_bread_count = 0
price_for_bread = price_for_1_kg_flour + price_for_1_pack_of_egg + price_for_1L_milk / 4

while budget > price_for_bread:
    current_bread_count += 1
    colored_eggs += 3

    if current_bread_count % 3 == 0:
        colored_eggs -= (current_bread_count - 2)

    budget -= price_for_bread

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs "
      f"and {budget:.2f}BGN left.")



