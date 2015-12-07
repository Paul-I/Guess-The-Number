from __future__ import division
from random import randint
from os import system
from time import sleep
import sys,string

playing = True
guesses = 0
score = 0.0
num = randint(1,100)

def newGame():
    num = random.randint(1, 100)
    global num
    global guesses
    guesses = 0
    print "Do you want to play again [y/n]? "
    answer = raw_input()
    if (answer.strip() == "y"):
        newGame()
        return True
    if (answer.strip() == "n"):
        sys.exit(0)
    else:
        sys.exit(0)



print "Welcome to Paul's number guessing game!!!"
while(playing):
    system("cls")
    print "Guess a number between 1 and 100, have fun guessing"
    print ("What is your guess? ")
    guess=int(input())
    sleep(1)
    if (guess > 100 or guess < 1):
        invalid = True
        while (invalid):
            system("cls")
            print "You guess an invalid number please guess again"
            guess =int(input("What is your guess? "))
            guesses += 1
            if (100 >= guess >= 1):
                invalid = False
                guesses -= 1
    guesses += 1
    if (guess == num):
        score += (1000/guesses)
        print "Congratulation!!!!!!! You guessed the right number and it only took you " + str(guesses) + " guesses. Current score = " + str(int(score))
        sleep(2)
        playing = playAgain
    elif (guess > num):
        print "Your guess was too high sorry try again :("
        sleep(2)
    else:
        print "Your guess was too low sorry try again :("
        sleep(2)
