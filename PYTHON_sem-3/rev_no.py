#find rev of given no
n=int(input('Enter No '))
rem=0
temp = n
while (n!=0):
    rev= n%10
    rev = rev *10 +rem
    n=n/10
print(rev)