words = input('Enter a sentence: ').lower().split()
frequency = {}
unique = []
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
    if word not in unique:
        unique.append(word)
print('Frequency:', frequency)
print('Without repeated words:', unique)
