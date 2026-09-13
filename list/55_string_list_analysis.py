words = ['apple', 'banana', 'cat', 'orange', 'sky']
longest = words[0]
shortest = words[0]
vowel_start = []
consonant_end = []
for word in words:
    if len(word) > len(longest):
        longest = word
    if len(word) < len(shortest):
        shortest = word
    if word[0].lower() in 'aeiou':
        vowel_start.append(word)
    if word[-1].lower() not in 'aeiou':
        consonant_end.append(word)
print('Longest:', longest)
print('Shortest:', shortest)
print('Starts with vowel:', vowel_start)
print('Ends with consonant:', consonant_end)
