dictionary = {"shards": 0, "fragments": 0, "motes": 0}
materials = input().lower().split()
flag = False

while not flag:
    for index in range(0, len(materials), 2):
        key = materials[index + 1]
        value = int(materials[index])

        if key not in dictionary.keys():
            dictionary[key] = 0
        dictionary[key] += value

        if dictionary["shards"] >= 250:
            print("Shadowmourne obtained!")
            dictionary["shards"] -= 250
            flag = True
        elif dictionary["fragments"] >= 250:
            print("Valanyr obtained!")
            dictionary["fragments"] -= 250
            flag = True
        elif dictionary["motes"] >= 250:
            print("Dragonwrath obtained!")
            dictionary["motes"] -= 250
            flag = True
        if flag:
            break

    if flag:
        break

    materials = input().lower().split()

for key, value in dictionary.items():
    print(f"{key}: {value}")