"""Program 1.8: kilometre converter."""

kilometres = float(input("Enter distance in kilometres: "))
print("Metres:", round(kilometres * 1000, 2))
print("Centimetres:", round(kilometres * 100000, 2))
print("Miles:", round(kilometres * 0.621371, 2))
print("Feet:", round(kilometres * 3280.84, 2))
