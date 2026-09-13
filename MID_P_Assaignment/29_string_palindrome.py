"""Program 2.5: reverse strings and check palindromes."""
def reverse_string(text): return text[::-1]
def is_palindrome(text): return text.lower() == reverse_string(text).lower()

samples = ["madam", "racecar", "Your Name", "Your City"]
for text in samples:
    print(text, ": reverse =", reverse_string(text), ", palindrome =", is_palindrome(text))
