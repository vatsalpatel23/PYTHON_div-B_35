unit =int(input('Enter no of Units '))
if (unit<=100):
    bill= unit *2
elif (unit<=200):
    bill = (100*2) + (unit-100) *3
elif (unit<=300):
    bill = (100*2)+ (100*3) + (unit-100) *5
else :
    bill = (100*2)+ (100*3) +(100*5) + (unit-100) *7

print('Total amount of bill is =₹',bill)