command = input()
dictionary = {}

while command != "End":
    company_name, employee_id = command.split(" -> ")

    if company_name not in dictionary.keys():
        dictionary[company_name] = []
    if employee_id not in dictionary[company_name]:
        dictionary[company_name].append(employee_id)

    command = input()

for key, value in dictionary.items():
    print(f"{key}")
    for element in value:
        print(f"-- {element}")

