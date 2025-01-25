import random

x=random.randint(1,100)
def intro():
    print("Let's play the guessing game!")
    name=input("What is your name?")
    print("In this game you have to guess a random number from 1 to 100 and you will get hints every time you guess wrong!Are you ready to play?,",name)
    if x%2==0:
        print("Your number is even")
    else:
        print("Your number is odd")
    print("Lets GO!")
def pick():
    chance_taken=0
    while chance_taken<6:
        try:
            guess=int(input("Guess the number"))
            if guess>=1 and guess <=100:
                chance_taken=chance_taken+1
                if chance_taken<6:
                    if guess<x:
                        print("Guess number is too low")
                    if guess>x:
                        print("Guess number is too high")
                    if guess!=x:
                        print("Try again")
                    if guess==x:
                        print("YOU WIN")
                        break
            if guess>100 or guess<1:
                print("Enter the number between 1 to 100")                
                    
        except:
            print("I do not think that is a number...retry")

play=True
while play:
    intro()
    pick()
    print("Do you want to play again")
    play=input("True or False")

    