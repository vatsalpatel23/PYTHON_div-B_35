words = ['madam', 'python', 'racecar', 'apple', 'level']
palindromes = list(filter(lambda word: word == word[::-1], words))
print(palindromes)
