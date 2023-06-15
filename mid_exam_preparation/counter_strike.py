initial_energy = int(input())
command = input()
won_battle_counter = 0

while command != "End of battle":

    command = int(command)

    if initial_energy >= command:
        initial_energy -= command
        won_battle_counter += 1
    else:
        print(f"Not enough energy! Game ends with {won_battle_counter} won battles and {initial_energy} energy")
        break

    if won_battle_counter % 3 == 0:
        initial_energy += won_battle_counter

    command = input()


else:
    print(f"Won battles: {won_battle_counter}. Energy left: {initial_energy}")


