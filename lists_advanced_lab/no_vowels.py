text = input()
vowels = ["a", "e", "u", "i", "o"]
my_list = [letter for letter in text if letter.lower() not in vowels]
print("".join(my_list))