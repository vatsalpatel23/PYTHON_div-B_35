def count_case(text):
    upper = 0
    lower = 0
    for character in text:
        if character.isupper():
            upper += 1
        elif character.islower():
            lower += 1
    return (upper, lower)
text = input('Enter text: ')
upper, lower = count_case(text)
print('Uppercase:', upper)
print('Lowercase:', lower)
