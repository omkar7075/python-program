a

#slip no 9
#largest number





a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))

if(a>= b) and (a>= c):
    largest=a
elif(b >=a)and (b >=c):
    largest=b
else:
    largest=c
print("the largest number:",largest)
