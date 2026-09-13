n=int(input('Enter No '))
temp=n
sum = 0
while temp>0:
    re=temp%10
    sum+=re**3
    temp//=10
    if(n==sum):
        print(n,"The number is armstrong")
    else:
        print(n,"The number is not armstrong")
