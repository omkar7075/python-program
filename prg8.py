#area of triangle
print("#####################################Area of triangle################################################","\n")
b=int(input("Enter Base:"))
h=int(input("Enter Height:"))

t=b*h/2
print("Area of Triangle:","\n",t)
print("\n")

#Area of Circle
print("#####################################Area of circle################################################","\n")
r=int(input("Enter Radius:"))
pi=3.14

c=pi*r*r
print("Area of Circle:","\n",c)
print("\n")


#swap values of two variable

print("#####################################swap variables################################################","\n")

a=int(input("Enter Number:"))
b=int(input("Enter Number:"))
print("before swapping variable:","\n",a,"\n",b)
temp=a
a=b
b=temp
print("after swapping variable:","\n",a,"\n",b)
print("\n")


#fibonacci series
print("#####################################fibonacci series################################################","\n")

n=int(input("Enter Number:"))
n1,n2=0,1
print("Fibinacci Series:","\n",n1,"\n",n2,end="")

for i in range(0,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,"\n")
print()    

print("\n")
