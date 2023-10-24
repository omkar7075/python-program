#slip no 18
#zero error exception
print("zeroerror exception")
n=10
m=0
try:
    n/m
except:
    print("can't divide by zero")
else:
    print(n/m)


print("\n")
#slip no 19
#prime number
print("prime number")
num=int(input("enter number:"))
flag=False

if num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break

if flag:
    print("prime number:",num)
else:
     print("prime not number:",num)
    

print("\n")
#slip no 20
#square perimeter
print("square area perimeter")
n=int(input("enter number:"))
area=n*n
print("area of square:",area)
per=4*n
print("perimeter of square",per)
