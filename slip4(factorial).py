#slip no 4
#factorial

n=int(input("enter number:"))
def check_fact(n):
    fact=1
    if n<0:
        print("negative number")
    elif(n==0):
        print("factorial is 0")
    else:
        for i in range(1,n+1):
            fact=fact*i
            print("factorial:",fact)
check_fact(n)
