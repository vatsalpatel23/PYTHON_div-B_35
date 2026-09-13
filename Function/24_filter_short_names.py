students = ['Amit', 'Bhavna', 'Dax', 'Kiran', 'Rohit']
result = list(filter(lambda name: len(name) < 6, students))
print(result)
