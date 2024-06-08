import random as rn
n=input("Enter a number:")
if n.isdigit():
    n=int(n)
    if n==0:
        print("Please enter a larger number.")
        quit()
else:
    print("Please enter a number.")
    quit()
guesses=0
r=rn.randrange(n)
print(r)
while True:
    guesses+=1
    u=input("Guess a number:")
    if u.isdigit():
        u=int(u)
    else:
        print("Please enter a number.")
        continue
    if u==r:
        print("You got it in",guesses,"time!!")
        break
    elif u>n:
        print("You are above the number.")
    else:
        print("You are below the number.")
    print("Better Luck next time.\n")
        



