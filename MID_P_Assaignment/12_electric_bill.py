"""Program 1.12: electric bill calculator."""

previous = float(input("Enter previous meter reading: "))
current = float(input("Enter current meter reading: "))
units = current - previous
if units < 0:
    print("Current reading cannot be less than previous reading.")
else:
    print("Units consumed:", round(units, 2))
    print("Total bill: Rs.", round(units * 5.50 + 100, 2))
