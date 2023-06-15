def loot(loots, some_items):
    for item in some_items:
        if item not in loots:
            loots.insert(0, item)
    return loots


def drop(loots, some_index):
    if some_index in range(len(loots)):
        removed_loot = loots.pop(some_index)
        loots.append(removed_loot)
    return loots


def steal(loots, some_count):
    if some_count >= len(loots):
        print(", ".join(loots))
        loots = []
    else:
        stolen_index = len(loots) - some_count
        stolen_items = loots[stolen_index:]
        print(", ".join(stolen_items))
        loots = loots[0:stolen_index]
    return loots


treasure_chest = input().split("|")
command = input()

while command != "Yohoho!":
    command = command.split()

    if command[0] == "Loot":
        items = command[1:]
        treasure_chest = loot(treasure_chest, items)
    elif command[0] == "Drop":
        index = int(command[1])
        treasure_chest = drop(treasure_chest, index)
    elif command[0] == "Steal":
        count = int(command[1])
        treasure_chest = steal(treasure_chest, count)

    command = input()


if not treasure_chest:
    print(f"Failed treasure hunt.")
else:
    average_treasure_gain = sum(len(item) for item in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")

