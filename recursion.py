#RECURSION

#print name n times
counter=0
n=int(input("enter n "))
namee=input("enter name ")
def name(namee,n,counter):
    if counter==n:
        return
    else:
        counter+=1
        print(namee)
        return name(namee,n,counter)
name(namee,n,counter)

#print 1 to N
counter=1
n=22
def printn(n,counter):
    if counter>n:
        return
    else:
        print(counter)
        return printn(n,counter+1)
printn(n,counter)

#print N to 1
n=22
counter=n
def printn(counter):
    if counter<1:
        return
    else:
        print(counter)
        return printn(counter-+1)
printn(counter)

#sum of n numbers
counter=0
n=22
sum=0
def sumofn(n,counter,sum):
    if counter>n:
        return sum
    else:
        sum+=counter
        return sumofn(n,counter+1,sum)
m=sumofn(n,counter,sum)
print(m)

#factorial
n=6
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(n))

#reverse an array
array=[1,4,5,3,2,3]
n=len(array)
for i in range(n//2):
    array[i],array[n-i-1]=array[n-i-1],array[i]
print(array)
    
#palindrome
p=""
s="NAAN"
n=len(s)
for i in range(n-1,-1,-1):
    p+=(s[i])
if p==s:
    print("palindrome")
else:
    print("No")