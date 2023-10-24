#slip no 14
#calculate lowercase,uppercase letter
s=str(input("enter string:"))
def check_case(s):
    l_case=0
    u_case=0
    for i in s:
        if i.isupper():
            u_case+=1
        if i.islower():
            l_case+=1
        print("lowercase:",l_case)
        print("uppercase:",u_case)
check_case(s)

