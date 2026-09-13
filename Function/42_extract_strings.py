def extract_string(string_list, length):
    return [word for word in string_list if len(word) >= length]
words = ['Python', 'list', 'exercises', 'practice', 'solution']
print(extract_string(words, 8))
