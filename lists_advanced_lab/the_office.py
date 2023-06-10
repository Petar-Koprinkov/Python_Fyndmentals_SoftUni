employees_happiness = [int(num) for num in input().split()]
factor = int(input())

new_list = list(map(lambda x: int(x) * factor, employees_happiness))
half_happiness = len(new_list) // 2
average_happiness = sum(new_list) / len(new_list)
counter = 0

for happiness in new_list:
    if happiness >= average_happiness:
        counter += 1

if counter >= half_happiness:
    print(f"Score: {counter}/{len(new_list)}. Employees are happy!")
else:
    print(f"Score: {counter}/{len(new_list)}. Employees are not happy!")




