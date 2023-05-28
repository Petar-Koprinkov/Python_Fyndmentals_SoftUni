first_string = input()
second_string = input()
third_string = input()

animals = [first_string, second_string, third_string]

animals[0], animals[2] = animals[2], animals[0]

print(animals)
