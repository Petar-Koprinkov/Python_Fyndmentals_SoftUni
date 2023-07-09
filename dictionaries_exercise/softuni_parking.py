number = int(input())
registered_cars = {}

for _ in range(number):
    data = input().split()
    command = data[0]
    name = data[1]
    if len(data) > 2:
        license_plate_number = data[2]

    if command == "register":
        if name not in registered_cars.keys():
            registered_cars[name] = license_plate_number
            print(f"{name} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif command == "unregister":
        if name not in registered_cars.keys():
            print(f"ERROR: user {name} not found")
        else:
            del registered_cars[name]
            print(f"{name} unregistered successfully")


for key, value in registered_cars.items():
    print(f"{key} => {value}")













