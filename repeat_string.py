string = input()
counter = int(input())

new_string = lambda a, b: a * b
result = new_string(string, counter)
print(result)