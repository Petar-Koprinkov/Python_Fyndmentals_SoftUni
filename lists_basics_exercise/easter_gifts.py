gifts = input().split(" ")
command_line = input()

while True:
    if command_line == "No Money":
        break

    command = command_line.split()
    if command[0] == "OutOfStock":
        gift = command[1]
        for elements in range(len(gifts)):
            if gift in gifts:
                index_of_gift = gifts.index(gift)
                gifts[index_of_gift] = "None"
    elif command[0] == "Required":
        gift = command[1]
        index = int(command[2])
        if index in range(len(gifts)):
            gifts[index] = gift
    elif command[0] == "JustInCase":
        gift = command[1]
        gifts[-1] = gift

    command_line = input()

for el in gifts:
    if el != "None":
        print("".join(el), end=" ")
