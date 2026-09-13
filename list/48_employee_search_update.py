employees = ['Aarav', 'Diya', 'Kabir']
name = input('Enter employee name: ')
if name in employees:
    employees[employees.index(name)] = input('Enter updated name: ')
else:
    employees.append(name)
print(employees)
