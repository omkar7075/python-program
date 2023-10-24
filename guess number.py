import random
number=random.randint(1,10)
print("Hey Champion:)")
print("> I remembered a number between 1 to 10 \n Rule is guess that number in 5 chances")
for i in range(0,5):
    user=int(input("GUESS THE NUMBER:"))
    if user==number:
        print("Hurry!!")
        print("you guessed the number right it's",number)
        break
if user!=number:
    print("Your guess is incorrect The number is:",number)
    
