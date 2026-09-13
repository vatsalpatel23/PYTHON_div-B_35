n=int(input('Enter No :'))
cou=0
for i in range(1,n+1):
    if n%i==0:
        cou += 1
if cou ==2:
    print("Prime num")
else:
    print("Not Prime num")