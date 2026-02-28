import random

choice=["rock","paper","scissors"]

you=input("select any one [rock,paper,scissors]: ").lower()
computer=random.choice(choice)

print(f"you chose:{you}\ncomputer chose: {computer}")

# If Elif Statment

if(you==computer):
    print("'it's tie'")

elif(you=="rock" and computer=="paper"):
    print("'You Lose!'")

elif(you=="paper" and computer=="rock"):
    print("'You Won!'")
    print("congratulations🎉")

elif(you=="rock" and computer=="scissors"):
    print("'You Won!'")
    print("congratulations🎉")

elif(you=="scissors" and computer=="rock"):
    print("'You Lose!'")

elif(you=="paper" and computer=="scissors"):
    print("'You Lose!'")
    
elif(you=="scissors" and computer=="paper"):
    print("'You Won!'")
    print("congratulations🎉")

else:
    print("Something went wrong! \n'please check speeling'")











