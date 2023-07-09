command = input()
dictionary = {}

while True:
    if command == "Lumpawaroo":
        break

    if " | " in command:
        force_side, force_user = command.split(" | ")

        for key, value in dictionary.items():
            if force_user in value:
                break

        else:
            if force_side not in dictionary.keys():
                dictionary[force_side] = []
            dictionary[force_side].append(force_user)

    if " -> " in command:
        force_side, force_user = command.split(" -> ")

        for key, value in dictionary.items():
            if force_user in value:
                if force_side not in dictionary.keys():
                    dictionary[force_side] = []
            dictionary[key].remove(force_user)
            dictionary[key].append(force_user)
            break
        else:
            if force_side not in dictionary.keys():
                dictionary[force_side] = []
            dictionary[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

    command = input()

for key, value in dictionary.items():
    if dictionary[key]:
        print("Side: {key}, Members: {len(value)}")
        for el in value:
            print(f"! {el}")





