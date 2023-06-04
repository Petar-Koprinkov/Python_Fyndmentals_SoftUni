def perfect_number(some_number):
    sum_of_divisors = 0
    for digit in range(1, some_number):
        if some_number % digit == 0:
            sum_of_divisors += digit
    if some_number == sum_of_divisors:
        return f"We have a perfect number!"
    return f"It's not so perfect."


number = int(input())
print(perfect_number(number))