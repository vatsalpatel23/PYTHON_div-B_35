values = ['Python', None, '', 'Java', 0, [], 'List']
cleaned = []
for value in values:
    if value is not None and value != '':
        cleaned.append(value)
print(cleaned)
