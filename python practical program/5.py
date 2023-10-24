#practiucal no5

#Program to count the occurrences of each word in a given string sentence.

l = dict()
user = input(" Enter a string: ")
user1 = user.split()
for i in user1:
    if not i in l:
        l[i] = 1
    else:
        l[i] = l[i] + 1
print(l[i], l)
