import re
valid_url = []

text = input()
pattern = r"\b((?P<sub_domain>www)\.(?P<domain>[A-Za-z\-0-9]+)(?P<extension>\.[a-z]+)+)\b"

while text:
    results = re.search(pattern, text)

    if results:
        valid_url.append(results.group(1))

    text = input()

for link in valid_url:
    print(link)

