#This is just a division system, the only reason I have it is because of the score function so it can do the division to get the code.
from __future__ import division
#This is what makes the game to generate numbers
from random import randint
#This function is only to clean the command line that you are using so it doesn't look too messy.
from os import system
#This function has to do with the last one, this just to set how many seconds it should wait before it cleans up.
from  time import sleep

#This is just the beginning of the game yah
playing = True
#This tells the computer to only choose the random number between 1 and 100 but it can be either 1 or 100 too.
num = randint(1,100)
#This is saying how many time we've guesses and it also reset the guesses to zero once you find the number.
guesses = 0
#This function is for the score and it set to zero right now.
score = 0.0


#This what make it possible to playagain as simple as it says "playagain".
def playAgain():
#This is what ask you do you want to play again or not it also allows you to choose.
    answer = raw_input("Do you want to play again [y/n]?")
#The next three line are saying if your answer is yes then it allows to play again start a new game.
    if (answer.strip() == "y"):
        newGame()
        return True
#And if the answer is no then it will exit from the game.
    elif (answer.strip() == "n"):
        return False
#Same as if your answer is yes it allows you to play again
    else:
        return playAgain()

#After you made your choice and choose yes this starts the new game and I already explained the 4 line.
def newGame():
    global num
    num = randint(1,100)
    global guesses
    guesses = 0

#This is telling the computer what to display on your screen.
print ("Welcome to Paul's Guessing Game, have  fun!!!")
while(playing):
#This what cleans up the screen so it won't look messy and this will change depending on the OS you are using.
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
#This takes off guesses
                guesses -= 1
#This add to the amount of guesses I have guessed and this is how I find out how many guesses you've guessed.
    guesses += 1
    if (guess == num):
#This is how I get the scores by dividing the number of guesses by 1000, this is why I need the code from future import division.
        score += (1000/guesses)
        print "Congratulations!!!!!!! The number you guess was right and it took you only " + str(guesses) + "guesses. Current score = " + str(int(score))
        sleep(2)
        playing = playAgain()
    elif (guess > num):
        print "Your guess was too high!!! sorry please try again"
        sleep(2)
    else:
        print "Your guess was too low!!! sorry please try again"

        sleep(2)
