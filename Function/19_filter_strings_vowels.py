items = [10, 'Python', 'Apple', 20, 'Orange', 'List']
strings = list(filter(lambda item: type(item) == str, items))
text = 'Hello Python World'
without_vowels = ''.join(filter(lambda character: character.lower() not in 'aeiou', text))
print('Strings:', strings)
print('Without vowels:', without_vowels)
