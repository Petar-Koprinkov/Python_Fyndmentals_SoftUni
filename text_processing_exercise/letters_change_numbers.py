string = input().split()
total_sum = 0
for element in string:
    front_letter = element[0]
    back_letter = element[-1]
    number = int(element[1:-1])

    if front_letter.isupper():
        front_letter_position = ord(front_letter) - 64
        total_sum += number / front_letter_position
    elif front_letter.islower():
        front_letter_position = ord(front_letter) - 96
        total_sum += number * front_letter_position
    if back_letter.isupper():
        back_letter_position = ord(back_letter) - 64
        total_sum -= back_letter_position
    elif back_letter.islower():
        back_letter_position = ord(back_letter) - 96
        total_sum += back_letter_position

print(f"{total_sum:.2f}")




