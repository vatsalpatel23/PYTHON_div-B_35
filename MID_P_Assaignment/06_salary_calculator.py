"""Program 1.6: salary calculator."""

basic = float(input("Enter basic salary: "))
hra = basic * 0.20
da = basic * 0.10
pf = basic * 0.12
gross = basic + hra + da
print("Gross salary:", round(gross, 2))
print("Net salary:", round(gross - pf, 2))
