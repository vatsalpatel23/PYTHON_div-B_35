sentence = input('Enter a sentence: ')
words = sentence.split()
long_words = [word for word in words if len(word) > 5]
print(long_words)
