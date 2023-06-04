def characters(char1, char2):
    numbers_list = []
    for char in range(ord(char1) + 1, ord(char2)):
        numbers_list.append(chr(char))
    return " ".join(numbers_list)


first_character = input()
second_character = input()
print(characters(first_character, second_character))
