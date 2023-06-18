def move(message, letter_number):
    move_characters = message[0:letter_number]
    new_word = message[letter_number:]
    message = new_word + move_characters
    return message


def insert(message, current_index, current_value):
    for char in current_value:
        current_index += 1
        message.insert(current_index, char)
    return message


def change_all(message, old_str, new_str):
    for i in range(len(message)):
        if message[i] == old_str:
            message[i] = new_str
    return message


encrypted_message = [word for word in input()]
command = input()

while command != "Decode":
    command = command.split("|")

    if command[0] == "Move":
        number_of_letters = int(command[1])
        encrypted_message = move(encrypted_message, number_of_letters)
    elif command[0] == "Insert":
        index = int(command[1]) - 1
        value = [character for character in command[2]]
        encrypted_message = insert(encrypted_message, index, value)
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = change_all(encrypted_message, substring, replacement)

    command = input()

new_message = "".join(encrypted_message)
print(f"The decrypted message is: {new_message}")
