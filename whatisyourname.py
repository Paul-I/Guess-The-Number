from time import sleep

print "This is a game where you write your name and other stuff"
sleep(1)

given_name = raw_input("What is your first name? ")
family_name = raw_input("What is your last name? ")
phone_number = raw_input("What is your phone number? ")
email_address = raw_input("What is your email address? ")
home_address = raw_input("What is your home address? ")

print "So, your given name is %s, family name is %s, and the phone number is %s. Also your email address is %s, and your home address is %s." % (given_name, family_name, phone_number, email_address, home_address)


txtYourInfo = given_name.lower() + family_name + '.txt'
Yourinfo = open(txtYourInfo, 'w')


Yourinfo.write (given_name)
Yourinfo.write ("\ ")
Yourinfo.write ("\n ")
Yourinfo.write (family_name)
Yourinfo.write ("\n ")
Yourinfo.write (phone_number)
Yourinfo.write ("\n ")
Yourinfo.write (email_address)
Yourinfo.write ("\n ")
Yourinfo.write (home_address)



def playAgain():
    answer = raw_input("Do you want to play again [y/n]? ")
    if (answer.strip() == "y"):
        newGame()
        return True
    elif (answer.strip() == "n"):
        return False

    else:
        playAgain
