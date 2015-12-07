from __future__ import division
from random import randint
from os import system
from  time import sleep

playing = True
num = randint(1,100)
guesses = 0
score = 0.0


def playAgain():
    answer = raw_input("Do you want to play again [y/n]?")
    if (answer.strip() == "y"):
        newGame()
        return True
    elif (answer.strip() == "n"):
        return False
    else:
        return playAgain()

def newGame():
    global num
    num = randint(1,100)
    global guesses
    guesses = 0

print ("Welcome to Paul's Guessing Game, have  fun!!!")
while(playing):
    system("cls")
    print "Guess a number between 1 and 100, good luck!!!"
    guess = int(raw_input("What is your guess? "))
    sleep(1)
    if (guess > 100 or guess < 1):
        invalid = True
        while(invalid):
            system ("cls")
            print "You put an INVALID NUMBER!!!! Please guess a number between 1 and 100"
            guess = int(raw_input("What is your guess? "))
            guesses += 1
            if (100 >= guess >= 1):
                invalid = False
                guesses -= 1
                guesses += 1
    if (guess == num):
        score += (1000/guesses)     
        print "Congratulations!!!!!!! The number you guess was right and it took you only " + str(guesses) + "guesses. Current Score = " + str(int(score))
        sleep(2)
        playing = playAgain()
    elif (guess > num):
        print "Your guess was too high!!! sorry please try again"
        sleep(2)
    else:
        print "Your guess was too low!!! sorry please try again"
        sleep(2)
