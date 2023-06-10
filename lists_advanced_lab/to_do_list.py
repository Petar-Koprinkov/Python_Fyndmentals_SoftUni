my_list = [0] * 10 # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:

    command = input()

    if command == "End":
        break

    command = command.split("-")
    action = command[1]
    index = int(command[0]) - 1
    if index in range(len(my_list)):
        my_list[index] = action

new_list = [elements for elements in my_list if elements != 0]

print(new_list)

