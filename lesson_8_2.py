import string

def is_palindrome(s):
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1]

# Приклади використання:
print(is_palindrome("A man, a plan, a canal, Panama"))
print(is_palindrome("OP"))
print(is_palindrome("a."))
print(is_palindrome("aurora"))
