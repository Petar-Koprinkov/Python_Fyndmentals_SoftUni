first_word = input()
second_word = input()
last_printed_word = first_word

for currents_string in range(len(first_word)):
    left_part = second_word[:currents_string + 1]
    right_part = first_word[currents_string + 1:]

    new_word = left_part + right_part

    if new_word == last_printed_word:
        continue
    print(new_word)

    last_printed_word = new_word








