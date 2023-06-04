def factorial(some_number):
    result = 1
    for digit in range(1, some_number + 1):
        result *= digit
    return result


first_number = int(input())
second_number = int(input())
first_factorial = factorial(first_number)
second_factorial = factorial(second_number)
total_result = first_factorial / second_factorial
print(f"{total_result:.2f}")