MAX_CAPACITY = 4
people = int(input())
lift = [int(x) for x in input().split()]

for cabin in range(len(lift)):

    free_spaces = MAX_CAPACITY - lift[cabin]

    if people >= MAX_CAPACITY:
        lift[cabin] += free_spaces
    else:
        lift[cabin] += people

    people -= free_spaces

    if people <= 0 and (cabin != len(lift) - 1 or lift[cabin] < MAX_CAPACITY):
        print("The lift has empty spots!")
        break

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")

print(*lift, sep=" ")

