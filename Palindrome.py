word = input("Enter sequence ")

palindrome = word[::-1]

if word == palindrome:
    print("palindrome")
else:
    print("not palindrome")