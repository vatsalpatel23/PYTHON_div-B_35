def find_string(string1, string2='all'):
    positions = []
    start = 0
    while True:
        position = string1.find(string2, start)
        if position == -1:
            break
        positions.append(position + 1)
        start = position + 1
    return positions
text = 'Hello all, Good Morning to all.'
word = input('Enter word (press Enter for all): ') or 'all'
positions = find_string(text, word)
print('Positions:' if positions else 'String not found.', positions)
