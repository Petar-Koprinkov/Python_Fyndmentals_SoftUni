def odd_and_even_sum(some_number):
    odd_sum = 0
    even_sum = 0
    for digits in some_number:
        if int(digits) % 2 == 0:
            even_sum += int(digits)
        else:
            odd_sum += int(digits)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
print(odd_and_even_sum(number))



