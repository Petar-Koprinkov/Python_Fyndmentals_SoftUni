level_of_fire = input().split("#")
amount_of_water = int(input())
total_effort = 0
total_fire = 0
list_fire = []


for fire in level_of_fire:
    type_of_fire, value_of_cell = fire.split(" = ")
    value_of_cell = int(value_of_cell)

    flag = False

    if type_of_fire == "High":
        if value_of_cell in range(81, 125 + 1):
            flag = True
    elif type_of_fire == "Medium":
        if value_of_cell in range(51, 80 + 1):
            flag = True
    elif type_of_fire == "Low":
        if value_of_cell in range(1, 50 + 1):
            flag = True

    if flag:
        if amount_of_water >= value_of_cell:
            amount_of_water -= value_of_cell
            effort = value_of_cell * 0.25
            total_effort += effort
            total_fire += value_of_cell
            list_fire.append(value_of_cell)

print("Cells:")

for fires in list_fire:
    print(f" - {fires}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")






