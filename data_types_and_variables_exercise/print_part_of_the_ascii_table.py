first_line = int(input())
last_line = int(input())

for index in range(first_line, last_line + 1):
    character = chr(index)
    print(character, end= " ")
