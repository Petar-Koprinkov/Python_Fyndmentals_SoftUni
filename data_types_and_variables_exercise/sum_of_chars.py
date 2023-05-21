number_of_lines = int(input())
total_sum = 0

for _ in range(number_of_lines):
    characters = input()
    value = ord(characters)
    total_sum += value

print(f"The sum equals: {total_sum}")


