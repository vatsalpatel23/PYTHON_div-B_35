#find sum of given no
i=1
sum=0
n=int(input('Enter No '))
while i<=n:
    n= n%10
    sum = sum + i
    i=i+1
print(sum)