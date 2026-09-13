"""Program 2.6: vowel and character frequency functions."""
def count_vowels(text): return sum(char.lower() in "aeiou" for char in text)
def char_frequency(text):
    counts = {}
    for char in text: counts[char] = counts.get(char, 0) + 1
    return counts

sentence = input("Enter a sentence: ")
print("Vowels:", count_vowels(sentence))
print("Character frequency:", char_frequency(sentence))
