string = input()
digit_line = ""
letter_line = ""
character_line = ""

for char in string:
    if char.isdigit():
        digit_line += char
    elif char.isalpha():
        letter_line += char
    else:
        character_line += char


print(digit_line)
print(letter_line)
print(character_line)