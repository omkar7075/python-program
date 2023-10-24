#practical no 8
"""Program to count the frequency of words appearing in a
string using a dictionary.
"""

my_string = input("Enter the string :")
my_list=[]
my_list=my_string.split()
word_freq=[my_list.count(p) for p in my_list]
print("The frequency of words is ...")
print(dict(zip(my_list,word_freq)))
