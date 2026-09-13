def multiply_numbers(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product
numbers = [2, 3, 4, 5]
print('Product:', multiply_numbers(numbers))
