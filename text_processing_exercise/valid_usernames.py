def length(current_username):
    if 3 <= len(current_username) <= 16:
        return True
    return False


def contain(current_username):
    for element in current_username:
        if not (element.isalnum() or element == "_" or element == "-"):
            return False
    return True


def redundant(current_username):
    if " " in current_username:
        return False
    return True


def all_valid(current_username):
    if length(current_username) and contain(current_username) and redundant(current_username):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if all_valid(username):
        print(username)
