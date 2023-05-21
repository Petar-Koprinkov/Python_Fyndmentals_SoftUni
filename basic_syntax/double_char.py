while True:
    current_word = input()

    if current_word == "End":
        break
    if current_word == "SoftUni":
        continue

    new_word = ""

    for character in current_word:
        new_word += character * 2

    print(new_word)

