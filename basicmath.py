#number of digits
n=input("enter digit")
n=str(n)
print(len(n))

#reverse number
n=int(input("enter num "))
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)

#number palindrome
n=int(input("enter num "))
rev=0
num=n
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
if num==rev:
    print("palindrome")
else: print("Not a palindrome")

#GCD
n=int(input("enter num "))
rev=0
num=n
while n!=0:
    rem=n%10
    rev+=rem**3
    n=n//10
if rev==num:
    print("true")
else:
    print('false')

#find all divisors
n=int(input("enter num "))
p=[]
for i in range(1,n+1):
    if n%i==0:
        p.append(i)
print(p)

#check for prime
n=int(input("enter num "))
isprime=1
for i in range(2,n//2+1):
    if n%i==0:
        isprime=0
if isprime==1:
    print("prime")
else:
    print('not prime')
