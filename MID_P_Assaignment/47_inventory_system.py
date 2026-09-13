"""Program 3.11: simple inventory using functions."""
inventory = {"pen": 10, "notebook": 3, "eraser": 6}
def add_item(name, quantity): inventory[name] = inventory.get(name, 0) + quantity
def remove_item(name): return inventory.pop(name, "Item not found")
def update_qty(name, quantity): inventory[name] = quantity
def display_inventory():
    for name, quantity in sorted(inventory.items()): print(name + ":", quantity)
def low_stock(): return {name: qty for name, qty in inventory.items() if qty < 5}

add_item("pencil", 4)
update_qty("pen", 8)
remove_item("eraser")
display_inventory()
print("Low stock:", low_stock())
