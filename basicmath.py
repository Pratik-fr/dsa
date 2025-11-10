#number od digits
n=input("enter digit")
# n=str(n)
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


