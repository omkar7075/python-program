
#slip no.1
#fibonacci series
print("fibonacci: \n")
n=int(input("Enter Number:"))
n1=0
n2=1
count=0
if n<=0:
    print("positive number")
elif n==1:
    print("Fibonacci series:","\n",n,":",end="")
    print(n1)
else:
     print("Fibonacci series:")

while (count<n):
    print(n1,end="")
    n3=n1+n2
    n1=n2
    n2=n3
    count+=1
    
#slip no 2
    #swap  tuple
print("\n swap tuple:\n")
a=10
b=20
print("before swapping:",a,b)
temp=a
a=b
b=temp
print("after swapping:",a,b)
