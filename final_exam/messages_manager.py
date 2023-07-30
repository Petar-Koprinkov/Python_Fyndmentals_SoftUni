def add(current_dict, current_command):
    username = current_command[1]
    sent = int(current_command[2])
    received = int(current_command[3])
    if username not in current_dict.keys():
        current_dict[username] = [sent, received]
    return current_dict


def message(current_dict, current_command):
    sender = current_command[1]
    receiver = current_command[2]
    if sender in current_dict.keys() and receiver in current_dict.keys():
        current_dict[sender][0] += 1
        current_dict[receiver][1] += 1
        if current_dict[sender][0] + current_dict[sender][1] >= capacity:
            print(f"{sender} reached the capacity!")
            del current_dict[sender]
        if current_dict[receiver][1] + current_dict[receiver][0] >= capacity:
            print(f"{receiver} reached the capacity!")
            del current_dict[receiver]
    return current_dict


def empty(current_dict, current_command):
    username = current_command[1]
    if username == "All":
        del current_dict
        return {}
    elif username in current_dict.keys():
        del current_dict[username]
    return current_dict


capacity = int(input())
command = input()
dictionary = {}

while command != "Statistics":
    command = command.split("=")
    action = command[0]

    if action == "Add":
        dictionary = add(dictionary, command)
    elif action == "Message":
        dictionary = message(dictionary, command)
    elif action == "Empty":
        dictionary = empty(dictionary, command)
    command = input()

print(f"Users count: {len(dictionary)}")
for key, value in dictionary.items():
    print(f"{key} - {value[0] + value[1]}")