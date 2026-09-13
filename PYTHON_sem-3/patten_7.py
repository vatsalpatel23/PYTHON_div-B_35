w=5
for i in range(5,0,-1):
    for j in range(1,w):
        print(end="")
    w=w-1
    for j in range(1,i+1):
            print(j,end=" ")
    print()