def is_palindrome(word):
    reversed_string = word[::-1]
    if word == reversed_string:
        return True
    return False
