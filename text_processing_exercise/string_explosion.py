text = input()
power = 0
new_text = ""

for index in range(len(text)):
    if text[index] == ">":
        power += int(text[index + 1])
        new_text += text[index]
    elif power > 0 and text[index] != ">":
        power -= 1
    else:
        new_text += text[index]

print(new_text)
