number = int(input())
positive_list = []
negative_list = []

for _ in range(number):
    n = int(input())

    if n >= 0:
        positive_list.append(n)
    elif n < 0:
        negative_list.append(n)

positive_list_count = len(positive_list)
negative_list_sum = sum(negative_list)

print(positive_list)
print(negative_list)
print(f"Count of positives: {positive_list_count}")
print(f"Sum of negatives: {negative_list_sum}")


