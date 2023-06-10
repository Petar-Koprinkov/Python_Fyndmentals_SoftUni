def search_palindrome(some_text):
    if some_text == some_text[::-1]:
        return some_text


text = input().split()
palindrome = input()

new_list =[word for word in text if search_palindrome(word)]
palindrome_counter = new_list.count(palindrome)
print(new_list)
print(f"Found palindrome {palindrome_counter} times")

