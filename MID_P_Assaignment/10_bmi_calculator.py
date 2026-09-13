"""Program 1.10: BMI calculator."""

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in metres: "))
if height <= 0:
    print("Height must be greater than zero.")
else:
    bmi = weight / height ** 2
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    print("BMI:", round(bmi, 2), "(" + category + ")")
