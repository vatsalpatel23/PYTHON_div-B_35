"""Program 1.22: ATM PIN simulator."""
correct_pin = "1234"
attempts = 0
while attempts < 3:
    pin = input("Enter your 4-digit PIN: ")
    if pin == correct_pin:
        print("Access Granted")
        break
    attempts += 1
    print("Incorrect PIN")
else:
    print("Card Blocked")
