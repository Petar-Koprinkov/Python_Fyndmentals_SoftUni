n = int(input())
positive_number = []
negative_numbers = []
odd_numbers = []
even_numbers = []


for _ in range(n):
    number = int(input())

    if number >= 0:
        positive_number.append(number)
    if number < 0:
        negative_numbers.append(number)
    if number % 2 == 0:
        even_numbers.append(number)
    if number % 2 != 0:
        odd_numbers.append(number)

command = input()

if command == "negative":
    print(negative_numbers)
elif command == "positive":
    print(positive_number)
elif command == "even":
    print(even_numbers)
elif command == "odd":
    print(odd_numbers)





