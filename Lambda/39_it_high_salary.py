employees = [('Amit', 'IT', 55000), ('Bina', 'HR', 62000), ('Dax', 'IT', 48000), ('Diya', 'IT', 72000)]
result = list(filter(lambda employee: employee[1] == 'IT' and employee[2] > 50000, employees))
print(result)
