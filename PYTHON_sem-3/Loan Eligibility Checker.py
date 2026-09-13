Income=int(input("Enter Income "))
if Income>=100000:
    print('Premium Loan')   
elif Income>=50000:
    print('Standard Loan')
elif Income>=25000:
    print('Basic Loan')
else :
    print('Not Eligible')
