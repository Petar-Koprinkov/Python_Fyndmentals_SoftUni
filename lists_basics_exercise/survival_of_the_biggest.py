list_of_integers = input().split()
count_of_remover = int(input())
list_as_digits = []
list_as_string = []

for digit in list_of_integers:
    list_as_digits.append(int(digit))

for remover in range(count_of_remover): 
    list_as_digits.remove(min(list_as_digits))

for index in list_as_digits:
    list_as_string.append(str(index))

new_string = ", ".join(list_as_string)
print(new_string)

