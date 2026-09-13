"""Program 1.4: Celsius to Fahrenheit and Kelvin."""

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15
print("Fahrenheit:", round(fahrenheit, 2), "F")
print("Kelvin:", round(kelvin, 2), "K")
