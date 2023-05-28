n = int(input())
special_word = input()
first_list = []
second_list = []

for _ in range(n):
    strings = input()
    first_list.append(strings)

    if special_word in strings:
        second_list.append(strings)

print(first_list)
print(second_list)

