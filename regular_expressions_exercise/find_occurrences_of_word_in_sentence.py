import re

text = input()
word = input()

pattern = rf"\b{word}\b"

matches = re.findall(pattern, text, re.IGNORECASE)

result = len(matches)

print(result)