import re

text = input()

pattern = r"(?P<Date>\d{2})(?P<Separator>[\.\-/])([A-Z][a-z]{2})(?P=Separator)(\d{4})"

matches = re.finditer(pattern, text)

for match in matches:
    day = match.group(1)
    separator = match.group(2)
    month = match.group(3)
    year = match.group(4)
    print(f"Day: {day}, Month: {month}, Year: {year}")