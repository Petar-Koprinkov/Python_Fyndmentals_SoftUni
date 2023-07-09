text = input()
new_character = ""

for character in text:
    if new_character != character:
        print(character, end="")
    new_character = character

