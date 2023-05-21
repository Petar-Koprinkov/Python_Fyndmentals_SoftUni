coffee = 0

while True:
    command = input()

    if command == "END":
        break

    if command == "coding":
        coffee += 1
    elif command == "dog" or command == "cat":
        coffee += 1
    elif command == "movie":
        coffee += 1
    elif command == "CODING":
        coffee += 2
    elif command == "CAT" or command == "DOG":
        coffee += 2
    elif command == "MOVIE":
        coffee += 2
    else:
        continue

if coffee > 5:
    print(f"You need extra sleep")
else:
    print(f"{coffee}")



