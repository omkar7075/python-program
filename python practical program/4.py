#PRACTRICAL NO 4
#Program to remove the ―i‖ th occurrence of the given word in a list where
#words repeat.


def removeword(lst,word,n):
    newlist=[]
    count=0

    #iterate the element
    for i in lst:
        if(i==word):
            count=count+1
            if(count!=n):
                newlist.append(i)
            else:
                newlist.append(i)
    lst=newlist

    if count ==0:
        print("item not found")
    else:
        print("updated list is :",lst)
    return newlist

#driner code

list["omkar","mayuresh","ganesh"]
word="omkar"
n=2

removeword(list,word,n)
