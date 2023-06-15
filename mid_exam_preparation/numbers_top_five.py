TOP = 5
number = [int(x) for x in input().split()]
average_numbers = sum(number) / len(number)
filtered_number = sorted([x for x in number if x > average_numbers])

if not filtered_number:
    print("No")
else:
    for _ in range(TOP):
        if filtered_number:
            print(filtered_number.pop(), end=" ")
