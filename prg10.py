#palidrome
print("############################ palidrome ###############################","\n")
n=int(input("Enter number:"))
temp=n
rev=0

while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10

if(temp==rev):
    print("palidrome")
else:
    print("not palidrome")
print("\n")

#year leap or not
print("############################ year is leap or not ###############################","\n")
y=int(input("Enter year:"))

if((y%4==0) and (y%100!=0) or (y%400==0)):
    print("leap")
else:
    print("not leap")
print("\n")

#tuples swap
print("############################swap the tuples###############################","\n")

t1=(1,2,3)
t2=(4,5,6)
print("before swaping tuple:","\n","t1:",t1,"\n","t2:",t2)
temp=t1
t1=t2
t2=temp
print("after swapping tuple:","\n","t1:",t1,"\n","t2:",t2)
