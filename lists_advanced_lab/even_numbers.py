my_list = list(map(int, input().split(", ")))
new_list = [index for index in range(len(my_list)) if my_list[index] % 2 == 0]
print(new_list)