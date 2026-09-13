def analyze_word(word):
    vowels = []
    for vowel in 'aeiou':
        count = word.lower().count(vowel)
        if count > 0:
            vowels.append({vowel: count})
    return {word.upper(): vowels, 'length': len(word)}
sentence = input('Enter a sentence: ')
analysis = list(map(analyze_word, sentence.split()))
print(analysis)
