numbers = [1, 2, 3, 2, 1]
palindrome = True
for index in range(len(numbers) // 2):
    if numbers[index] != numbers[-1 - index]:
        palindrome = False
print('Palindrome' if palindrome else 'Not palindrome')
