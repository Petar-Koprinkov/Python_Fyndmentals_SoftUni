text = input().upper()
new_text = ""
current_text = ""
numbers = ""


for index in range(len(text)):
    if not text[index].isdigit():
        current_text += text[index]
    else:
        numbers += text[index]
        new_text += current_text * int(numbers)
        current_text = ""
        numbers = ""

print(f"Unique symbols used: {len(set(new_text))}")
print(new_text)