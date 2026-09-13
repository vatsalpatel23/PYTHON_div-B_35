words = ['apple', 'banana', 'orange', 'sky', 'umbrella']
vowel_words = filter(lambda word: word[0].lower() in 'aeiou', words)
result = sorted(vowel_words, key=lambda word: len(word))
print(result)
