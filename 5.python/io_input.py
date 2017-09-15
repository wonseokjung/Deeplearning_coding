def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text==reverse(text)

something = input("Enter Text:")

if is_palindrome(something):
    print("Yes it is palidrome")
else:
    print("No, it is not a palindrome")




