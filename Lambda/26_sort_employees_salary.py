employees = [('Amit', 45000), ('Bina', 62000), ('Dax', 51000)]
result = sorted(employees, key=lambda employee: employee[1])
print(result)
