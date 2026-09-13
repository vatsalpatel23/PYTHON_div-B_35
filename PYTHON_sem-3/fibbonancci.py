#fibbonancci series upto n
n=int(input("Enter no")) 
a=0
b=1
c=None
print(a,end=" ")
print(b,end=" ")
while 1:
    c=a+b
    a=b
    b=c
    if(c>n):
        break
    else:
        print(c,end=" ")
    