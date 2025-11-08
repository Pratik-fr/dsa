n=6
for i in range(6):
    print(" "*(n-i),(2*i+1)*"*")
for i in range(6):
    print(' '*(5-i) + '*'*(2*i+1))
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(0,i*2-1):
        print("*",end="")
    for j in range(0,n-i):
        print(" ",end="")
    print()

for i in range(n,0,-1):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(0,i*2-1):
        print("*",end="")
    for j in range(0,n-i):
        print(" ",end="")
    print()
for i in range(1,n-1):
    print(i*"*")
for i in range(n-1,0,-1):
    print(i*"*")
for i in range(1,n):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print("1",end="")
        else:
            print("0",end="")
    print()
for i in range(2,n):
    for j in range(1,i):
        print(j,end="")
    for j in range(1,2*(n-i)-1):
        print(" ",end="")
    for j in range(1,i):
        print(i-j,end="")
    print()
p=1
for i in range(1,n):
    for j in range(1,i+1):
        print(p,end=' ')
        p+=1
    print()
t=65
for i in range(1,n):
    for j in range(n,0,-1):
        print(" ",end='')
    for j in range(1,i+1):
        print(chr(t),end=' ')
    print()
for i in range(1,n):
    for j in range(1,n-i):
        print("*",end="")
    for j in range(0,i):
        print(chr(t+j),end="")
    for j in range(i-1,0,-1):
        print(chr(t+j-1),end="")
    print()