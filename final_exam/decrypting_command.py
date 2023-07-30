def replace(current_string, current_command):
    char = current_command[1]
    new_char = current_command[2]
    current_string = current_string.replace(char, new_char)
    print(current_string)
    return current_string


def cut(current_string, current_command):
    start_index = int(current_command[1])
    end_index = int(current_command[2])
    if 0 <= start_index <= end_index < len(current_string):
        start_text = current_string[:start_index]
        end_text = current_string[end_index + 1:]
        current_string = start_text + end_text
        print(current_string)
        return current_string
    else:
        print(f"Invalid indices!")


def make(current_string, current_command):
    upper_lower = current_command[1]
    if upper_lower == "Upper":
        current_string = current_string.upper()
    elif upper_lower == "Lower":
        current_string = current_string.lower()
    print(current_string)
    return current_string


def check(current_string, current_command):
    substring = current_command[1]
    if substring in current_string:
        print(f"Message contains {substring}")
    else:
        print(f"Message doesn't contain {substring}")
    return current_string


def sum_result(current_string, current_command):
    start_index = int(current_command[1])
    end_index = int(current_command[2])
    total_sum = 0
    if 0 <= start_index <= end_index < len(current_string):
        substring = current_string[start_index:end_index + 1]
        for el in substring:
            total_sum += ord(el)
        print(total_sum)
    else:
        print("Invalid indices!")
    return current_string


string = input()
command = input()

while command != "Finish":
    command = command.split()
    action = command[0]

    if action == "Replace":
        string = replace(string, command)
    elif action == "Cut":
        string = cut(string, command)
    elif action == "Make":
        string = make(string, command)
    elif action == "Check":
        string = check(string, command)
    elif action == "Sum":
        string = sum_result(string, command)
    command = input()