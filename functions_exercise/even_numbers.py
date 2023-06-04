def even_number(some_number):
    if some_number % 2 == 0:
        return True


number = [int(num) for num in input().split()]

print(list(filter(even_number, number)))




