def chat(current_chat, current_message):
    current_chat.append(current_message)
    return current_chat


def delete(current_chat, current_message):
    if current_message in current_chat:
        current_chat.remove(current_message)
    return current_chat


def edit(current_chat, current_message, new_message):
    for i in range(len(current_chat)):
        if current_chat[i] == current_message:
            current_chat[i] = new_message
    return current_chat


def pin(current_chat, current_message):
    for i in range(len(current_chat)):
        if current_chat[i] == current_message:
            new_el = current_chat.pop(i)
            current_chat.append(new_el)
            break
    return current_chat


def spam(current_chat, messages):
    for element in messages:
        current_chat.append(element)
    return current_chat


command = input()
final_chat = []

while command != "end":

    command = command.split()

    if command[0] == "Chat":
        message = command[1]
        final_chat = chat(final_chat, message)
    elif command[0] == "Delete":
        message = command[1]
        final_chat = delete(final_chat, message)
    elif command[0] == "Edit":
        message = command[1]
        edit_message = command[2]
        final_chat = edit(final_chat, message, edit_message)
    elif command[0] == "Pin":
        message = command[1]
        final_chat = pin(final_chat, message)
    elif command[0] == "Spam":
        message = command[1:]
        final_chat = spam(final_chat, message)

    command = input()

for el in final_chat:
    print(el)



