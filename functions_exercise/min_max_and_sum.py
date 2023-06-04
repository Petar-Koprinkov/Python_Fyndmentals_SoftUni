numbers_as_string = input().split()
numbers_as_digits = []
for digit in numbers_as_string:
    numbers_as_digits.append(int(digit))

min_value = min(numbers_as_digits)
max_value = max(numbers_as_digits)
sum_value = sum(numbers_as_digits)

print(f"The minimum number is {min_value}")
print(f"The maximum number is {max_value}")
print(f"The sum number is: {sum_value}")