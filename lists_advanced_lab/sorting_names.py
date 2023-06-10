string_of_names = input().split(", ")
new_string = sorted(string_of_names, key= lambda x: (-len(x), x))
print(new_string)