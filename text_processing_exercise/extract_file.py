text = input().split("\\")
new_text = text[-1]
file, extension = new_text.split(".")
print(f"File name: {file}")
print(f"File extension: {extension}")