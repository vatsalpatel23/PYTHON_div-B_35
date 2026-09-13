models = [{'make': 'Nokia', 'model': 21, 'color': 'Black'}, {'make': 'Mi Max', 'model': 20, 'color': 'Gold'}, {'make': 'Samsung', 'model': 17, 'color': 'Blue'}]
result = sorted(models, key=lambda mobile: mobile['model'])
print(result)
