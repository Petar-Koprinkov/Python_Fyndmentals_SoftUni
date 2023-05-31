single_string_of_integers = input().split(", ")
count_of_beggars = int(input())
list_as_digit = []

for digit in single_string_of_integers:
    list_as_digit.append(int(digit))

final_list = []
start_index = 0

while start_index < count_of_beggars:
    sum_of_current_beggar = 0

    for money in range(start_index, len(list_as_digit), count_of_beggars):
        sum_of_current_beggar += list_as_digit[money]
    start_index += 1

    final_list.append(sum_of_current_beggar)

print(final_list)


