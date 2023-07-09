dictionary = {}

while True:
    phone = input()

    if "-" not in phone:
        break

    phone = phone.split("-")
    name, number = phone

    dictionary[name] = number

phone = int(phone)

for i in range(phone):
    contact = input()

    if contact in dictionary.keys():
        print(f"{contact} -> {dictionary[contact]}")
    else:
        print(f"Contact {contact} does not exist.")