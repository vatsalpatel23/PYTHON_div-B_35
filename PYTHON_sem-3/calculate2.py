#1-3+5-7+9-11 
n=int(input('Enter No '))
flag =1
sum = 0
for i in range(1,n+1,2): 
    sum = sum + (i*flag)
    flag=flag*-1
print(sum)