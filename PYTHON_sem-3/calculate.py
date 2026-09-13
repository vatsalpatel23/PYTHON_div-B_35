#1+2^2+3^3
n=int(input('Enter No '))
sum=0
for i in range(1,n+1):
    sum = sum + (i**i)
print(sum)