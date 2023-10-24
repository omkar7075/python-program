

#practical no. 10
# Program to find the length of a list using recursion

def strlength(s):
 if s=="":
     return(0)
 else:
     return(strlength(s[1:])+1)

str1=input("Enter string:")
l=strlength(str1)
print("String Length:",l)
