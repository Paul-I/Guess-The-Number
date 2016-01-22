from sys import exit


def start():


    name = raw_input("What is your name? ")
    print ("Hey "+name+"!!!! Welcome to Paul's game")
    print ("You are in front of a strange building known as SCS")

    choice = raw_input("Do you want to enter or retreat ? ")

    if (choice.strip() == "enter"):
        print("Welcome to SCS building, "+name+" this is a strange building so your goal is go through the building without dying")

        Playing()

    elif (choice.strip() == "retreat"):
        sys.exit

def Playing():
    print ("Now you are inside the glass")
    print ("There is two door in front of you one on the left and the other on you far right")

    choice = raw_input ("Which door do you want to enter ")

    firstfloor()

    if choice == "left":
        print ("Welcome to the main building from here on you can't turn back")
    elif choice == "right":
        print ("You entered the office and got eaten by the two huge dogs there. Good Job!!!")
    else:
        print ("Because you try to turn back you fell into a trap and your neck snap. Good Job!!!!!!")

def firstfloor():
    print ("Now you are at first floor and there is 4 ways you can go!!!!!")
    print ("There is a door on you right and on you left and there is two stair case in front of you one goes up and the other goes down.")

    choice = raw_input("Which path do you want to take!!!!!! Mwahahahhaha ")

    staircase()

    if choice == "right":
        print ("You saw the eyes of Dr. Johnson and died a painful death. Good Job!!!")
    elif choice == "left":
        print ("You sliped on the floor got bitting by a snake and died a poisonous death. Good Job!!!")
    elif choice == "down":
        print ("You slipped while on the stair case and smash your head into the wall but you didn't died and a bear came and rip your head off.")
    elif choice == "up":
        print ("Yah!!! You are still alive and you are on the stairs!!!!")

def staircase():
    print("There are many candies and gum on the stairs!!! delicious")

    choice = raw_input("Do want to eat the candies and gum, yes or no ")

    if choice == "yes":
        print ("You should know by now that if you eat gum or candies in SCS you pay 5,000, so you died cause you didn't have any money. Good Job!! ")
    elif choice == "no":
        print ("You know the rules well that you shouldn't eat gum in SCS so you live.")

        Secondfloor()


def Secondfloor():
    print ("Welcome to second floor be happy that you are still alive!!!!!! Mwahahahhaha")
    print ("There is door on your right and there is a glass door in front of you")
    print ("There is another door on the left and there is a staircase beside you")

    choice = raw_input("Which door do you want to go ? ")
    if choice == "left":
        print ("You are in the Chinese and you were asked a chinese question but you fail to answer so you got executed. Good Job!")
    elif choice == "right":
        print ("You are inside the toilet and you try to pup, you fell inside the toilet and got flushed by Johnson and died. Good Job!!!!")
    elif choice == "beside":
        print ("You have advance to the next level yahhhhh!!!! Well done"+name+"Good luck")

        hallway()

    elif choice == "glass door":
        print ("You are inside the hall way of second  fall.")

def hallway():
    print ("Welcome to the hall of death Mwahahahhaha and there is no turning back.")
    print ("Just walk straight and don't look back")
    print ("You are half way down the hall and you see a room do you enter, yes or no")

    choice = raw_input ("Do you want to enter the room? ")

    if choice == "yes":
        print ("You made the right choice")

        room()

    elif choice == "No":
        print ("You almost made the right choice but you didn't sorry :( died!!!!")

def rooms():
    print ("You are in a room and the door just locked")
    print ("Do you try and open a the door or keep moving")

    choice = raw_input("What do you want to do open door or keep moving")

    if choice == "open door":
        print ("You got electricuted and die a painful death")
    if choice == "keep moving":
        print ("Nice choice you are moving around in the room and you saw a big entrance")

        goingtoanotherroom()


def goingtoanotherroom():
    print ("You are still at the entrance thinking")
    print ("Do you walk through or click the sign that says ALARM")

    choice = raw_input("Do you click or walk through? ")

    if choice == "click":
        print ("Nice Job you did the right thing by destroying the alram system")

        strangeplace()

    elif choice == "walk through":
        print ("Sry you need to learn how to use your brain, you set the alarm off and got busted")

def strangeplace():
    print ("You've passed the big entrance and now you are in a strange place with 2 doors")
    print ("There is one door on the left and the other one on the right")


choice = raw_input("Which pathe do you want to takke, left or right? ")

if choice == "left":
    print ("Nice choice you are one room away from victory")

    lastroom()

if choice == "right":
    print ("How sad you were one room away from victory but you opened the wrong door and fall off the buils")

def lastroom():
    print ("You are inside the last room before victory")
    print ("There are two doors one on the left and one behind you")

    choice = raw_input("Which door do you want to open the left or behind")

    if choice == "left":
        print ("CONGRATULATIONS!!!!!!! You finished the game and you just open a room filled with God and Silver")
    elif choice == "behind":
        print ("You almsot made it but you open the wrong door which leads you to a giant dragon that burn your body")

start()
