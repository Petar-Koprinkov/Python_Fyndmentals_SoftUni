budget = int(input())

while True:
    command = input()
    if command == "End":
        print(f"You bought everything needed.")
        break
    command = int(command)

    if budget >= command:
        budget -= command
    else:
        print("You went in overdraft!")
        break
