def add(my_list, current_value):
    my_list.append(current_value)
    return my_list


def remove(my_list, current_value):
    for i in range(len(my_list)):
        if my_list[i] == current_value:
            my_list.pop(i)
            break
    return my_list


def replace(my_list, current_value, current_replacement):
    for i in range(len(my_list)):
        if my_list[i] == current_value:
            my_list[i] = current_replacement
            break
    return my_list


def collapse(my_list, current_value):
    my_list = [num for num in my_list if num >= current_value]
    return my_list


numbers_list = [int(number) for number in input().split()]
command = input()

while command != "Finish":
    command = command.split()

    if command[0] == "Add":
        value = int(command[1])
        numbers_list = add(numbers_list, value)
    elif command[0] == "Remove":
        value = int(command[1])
        numbers_list = remove(numbers_list, value)
    elif command[0] == "Replace":
        value = int(command[1])
        replacement = int(command[2])
        numbers_list = replace(numbers_list, value, replacement)
    elif command[0] == "Collapse":
        value = int(command[1])
        numbers_list = collapse(numbers_list, value)

    command = input()

print(*numbers_list)
