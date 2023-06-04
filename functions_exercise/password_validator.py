def password_validator(user_password):
    flag = True
    if len(user_password) < 6 or len(user_password) > 10:
        print(f"Password must be between 6 and 10 characters")
        flag = False
    if not user_password.isalnum():
        print(f"Password must consist only of letters and digits")
        flag = False
    counter_of_digit = 0
    for digit in user_password:
        if digit.isnumeric():
            counter_of_digit += 1
    if counter_of_digit < 2:
        print(f"Password must have at least 2 digits")
        flag = False

    return flag


password = input()
password_is_valid = password_validator(password)

if password_is_valid:
    print(f"Password is valid")