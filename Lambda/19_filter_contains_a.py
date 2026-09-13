words = ['python', 'apple', 'banana', 'list', 'java']
result = list(filter(lambda word: 'a' in word.lower(), words))
print(result)
