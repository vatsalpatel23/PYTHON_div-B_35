fruits = ['Apple', 'Banana', 'Mango']

def add_fruit(name):
    fruits.append(name)

def insert_fruit(name, position=1):
    fruits.insert(position, name)

def update_fruit(old_name, new_name):
    if old_name in fruits:
        fruits[fruits.index(old_name)] = new_name

def remove_fruit(value):
    if isinstance(value, int):
        fruits.pop(value)
    elif value in fruits:
        fruits.remove(value)

def arrange_fruits():
    fruits.sort()
add_fruit('Orange')
insert_fruit('Grapes')
update_fruit(old_name='Banana', new_name='Kiwi')
remove_fruit('Mango')
arrange_fruits()
print('Global variables:', list(globals().keys()))
print(fruits)
