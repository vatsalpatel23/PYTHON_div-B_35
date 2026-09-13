mobiles = {}

def create():
    global mobiles
    mobiles = {'Nokia': {'price': 5000, 'features': ['4G', 'Camera']}}

def add_mobile(name, price, features):
    mobiles[name] = {'price': price, 'features': features}

def update_mobile(name, price):
    if name in mobiles:
        mobiles[name]['price'] = price

def delete_mobile(name):
    if name in mobiles:
        del mobiles[name]
create()
add_mobile('Samsung', 18000, ['5G', 'AMOLED'])
update_mobile('Nokia', 5500)
delete_mobile('Samsung')
print(mobiles)
