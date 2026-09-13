employees = [{'name': 'Amit', 'salary': 45000}, {'name': 'Bina', 'salary': 62000}, {'name': 'Dax', 'salary': 51000}]
result = list(filter(lambda employee: employee['salary'] > 50000, employees))
print(result)
