import re

text = input()

pattern = r"((@|#)+([a-z]{3,})(@+|#+))\W*((\/+)(\d+)(\/+))"

matches = re.finditer(pattern, text)

for match in matches:
    print(f"You found {match.group(7)} {match.group(3)} eggs!")

