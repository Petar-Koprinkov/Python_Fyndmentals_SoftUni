def trains(some_train):
    while True:
        command = input()

        if command == "End":
            break

        command = command.split()

        if command[0] == "add":
            number_of_people = int(command[1])
            some_train[-1] += number_of_people
        elif command[0] == "insert":
            index = int(command[1])
            number_of_people = int(command[2])
            if index in range(len(some_train)):
                some_train[index] += number_of_people
        elif command[0] == "leave":
            index = int(command[1])
            number_of_people = int(command[2])
            if index in range(len(some_train)):
                some_train[index] -= number_of_people

    return some_train


number_of_wagons = int(input())
train = [0] * number_of_wagons

print(trains(train))