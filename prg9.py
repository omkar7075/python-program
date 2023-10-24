#for loop
print("#####################################for loop################################################","\n")
print("display a string in indexing:")
str="python"
for i in str:
    print("\n",i,end="")
print("\n")

#while loop
print("#####################################while loop############################","\n")
print("print the number by traversing:")
i=1
while(i<10):
    print("\n",i)
    i=i+1

print("\n")


#nested loop
print("#####################################nested loop##########################","\n")
print("############################nested for loop###############################","\n")
print("nested for loop to print row pattern:")
n=int(input("Enter Row Number:"))

for i in range(0,n):
    for j in range(i+1):
        print("*",end="")
    print()



print("\n")
print("############################nested while loop###############################","\n")

i=1
j=5
while(i<5):
    while(j<9):
        print(i,",",j)
        j=j+1  
        i=i+1

print("\n")

