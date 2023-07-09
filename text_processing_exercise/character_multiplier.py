text = input().split()
total_sum = 0

first_string, second_string = text

if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for second_index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[second_index])

if len(second_string) > len(first_string):
    for index in range(len(first_string)):
        total_sum += ord(second_string[index]) * ord(first_string[index])
    for second_index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[second_index])

if len(first_string) == len(second_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])

print(total_sum)