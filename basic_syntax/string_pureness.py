number = int(input())

for i in range(number):
    word = input()
    flag = True

    for j in range(len(word)):
        if word[j] == "P" or word[j] == "M" or word[j] == "S":
            print(f"This name is not available!")
            flag = False
            break
    if flag:
        print(f"This name is available!")




