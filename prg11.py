#variable output
print("##################variable output1 ##################","\n")
fruit="banana"
print("fruit=banana","\n")
print("fruit[:3]=",fruit[:3],"\n")
print("fruit[3:]=",fruit[3:],"\n")
print("fruit[3:3]=",fruit[3:3],"\n")
print("fruit[:]=",fruit[:],"\n")


print("##################variable output2 ##################","\n")
a=[1,2,3]
b=[4,5,6]
c=a+b
print("concatenation of a and b  :",c)
print("\n")


print("##################variable output3 ##################","\n")
a=[1,2,3]*3
print("repetation:",a)
print("\n")

print("##################variable output4 ##################","\n")
t=['a','b','c','d','e','f']
t[1:3]=['x','y']
print("using indexing add element:t=[a,b,c,d,e,f]",t)
