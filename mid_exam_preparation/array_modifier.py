def swap(my_list, first_index, second_index):
    my_list[first_index], my_list[second_index] = my_list[second_index], my_list[first_index]
    return my_list


def multiply(my_list, first_index, second_index):
    my_list[first_index] *= my_list[second_index]
    return my_list


def decrease(my_list):
    my_list = list(map(lambda x: x - 1, my_list))
    return my_list


initial_array_values = [int(num) for num in input().split()]
command = input()

while command != "end":
    command = command.split()

    if command[0] == "swap":
        index1 = int(command[1])
        index2 = int(command[2])
        initial_array_values = swap(initial_array_values, index1, index2)
    elif command[0] == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])
        initial_array_values = multiply(initial_array_values, index1, index2)
    elif command[0] == "decrease":
        initial_array_values = decrease(initial_array_values)

    command = input()

print(*initial_array_values, sep=", ")