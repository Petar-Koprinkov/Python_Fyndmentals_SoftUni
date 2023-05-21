number_of_lines = int(input())
TANK_CAPACITY = 255
counter = 0

for number in range(number_of_lines):
    litres_of_water = int(input())

    if TANK_CAPACITY < litres_of_water:
        print("Insufficient capacity!")

        continue
    else:
        TANK_CAPACITY -= litres_of_water
        counter += litres_of_water

print(counter)





