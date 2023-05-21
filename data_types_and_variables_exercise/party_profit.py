group_size = int(input())
days_of_adventure = int(input())
companions_count = group_size
coins = 0

for day in range(1, days_of_adventure + 1):

    if day % 10 == 0:
        companions_count -= 2
    if day % 15 == 0:
        companions_count += 5
    if day % 3 == 0:
        coins -= 3 * companions_count
    if day % 5 == 0:
        coins += 20 * companions_count
        if day % 3 == 0:
            coins -= 2 * companions_count

    coins += 50
    coins -= 2 * companions_count

coins_per_companion = coins // companions_count

print(f"{companions_count} companions received {coins_per_companion} coins each.")

