salaries = [35000, 45000, 52000, 60000]
high_salaries = filter(lambda salary: salary > 40000, salaries)
result = list(map(lambda salary: salary * 1.1, high_salaries))
print(result)
