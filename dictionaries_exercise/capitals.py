country = input().split(", ")
city = input().split(", ")
dictionary = {country[index]: city[index] for index in range(len(country))}
for key, value in dictionary.items():
    print(f"{key} -> {value}")