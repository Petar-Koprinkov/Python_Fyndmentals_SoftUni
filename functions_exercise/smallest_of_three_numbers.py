def smallest_number(numbers):
    result = min(numbers)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
my_list = [first_number, second_number, third_number]
print(smallest_number(my_list))