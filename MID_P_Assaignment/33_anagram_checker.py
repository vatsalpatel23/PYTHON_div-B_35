"""Program 2.9: anagram checker."""
def is_anagram(first, second):
    return sorted(first.replace(" ", "").lower()) == sorted(second.replace(" ", "").lower())

pairs = [("listen", "silent"), ("earth", "heart"), ("python", "typhon"), ("hello", "world")]
for first, second in pairs: print(first + ",", second + ":", is_anagram(first, second))
