
#practical no.6
#Program to check if a substring is present in a given string

import re
str1=str(input("enter the first string:"))
str2=str(input("enter the second string:"))

if(re.search(str2,str1)):
         print("yes, string '{0}' is present in string '{1}'" .format(str2,str1))
else:
    print("no, string '{0}' is not  present in string '{1}'" .format(str2,str1))
         

         
