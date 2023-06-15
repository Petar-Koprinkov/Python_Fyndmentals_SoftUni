def shoot(list_of_target, some_index, some_power):
    if some_index in range(len(list_of_target)):
        if list_of_target[some_index] <= some_power:
            list_of_target.pop(some_index)
        else:
            list_of_target[some_index] -= some_power
    return list_of_target


def add_value(list_of_target, some_index, some_value):
    if some_index in range(len(list_of_target)):
        list_of_target.insert(some_index, some_value)
    else:
        print("Invalid placement!")
    return list_of_target


def strike(list_of_target, some_index, some_radius):
    if some_index - radius in range(len(list_of_target)) and some_radius + radius in range(len(list_of_target)):
        list_of_target = list_of_target[0: some_index - radius] + list_of_target[some_index + radius + 1:]
    else:
        print("Strike missed!")
    return list_of_target


targets = [int(number) for number in input().split()]
command = input()

while command != "End":
    command = command.split()

    if command[0] == "Shoot":
        index = int(command[1])
        power = int(command[2])
        targets = shoot(targets, index, power)
    elif command[0] == "Add":
        index = int(command[1])
        value = int(command[2])
        targets = add_value(targets, index, value)
    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])
        targets = strike(targets, index, radius)

    command = input()


print(*targets, sep="|")