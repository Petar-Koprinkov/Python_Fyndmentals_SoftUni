def palindrome(some_number):
    if some_number == some_number[:: -1]:
        return True
    return False


number = input().split(", ")
for digit in number:
    print(palindrome(digit))