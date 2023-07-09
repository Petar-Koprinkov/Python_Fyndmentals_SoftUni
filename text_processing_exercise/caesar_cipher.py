text = input()
new_text = [chr(ord(char) + 3) for char in text]
print(*new_text, sep="")