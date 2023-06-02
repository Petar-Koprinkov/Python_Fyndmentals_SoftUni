def calculator(operator, first_number, second_number):

    result = 0

    if operator == "multiply":
        result = first_number * second_number
    elif operator == "divide":
        result = first_number // second_number
    elif operator == "add":
        result = first_number + second_number
    elif operator == "subtract":
        result = first_number - second_number

    return result


command = input()
num1 = int(input())
num2 = int(input())

print(calculator(command, num1, num2))