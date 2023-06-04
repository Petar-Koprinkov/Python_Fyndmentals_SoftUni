def sum_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(sum_num, num3):
    return sum_num - num3


def sum_and_subtract_numbers(num_one, num_two, num_three):
    sum_result = sum_numbers(num_one, num_two)
    sum_and_subtract_result = sum_result - num_three
    return sum_and_subtract_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(sum_and_subtract_numbers(first_number, second_number, third_number))