#!/usr/bin/python

import encryption
import random, datetime, os, time

def welcome():
    os.system("clear")
    print "Welcome to the Code Generator for your phone"
    os.system("cat asciiText.txt")
    print

welcome()

menuOption = raw_input("1 for generator\n2 to recover your passcode\n-->")
menuOption = int(menuOption)

if menuOption == 1:
    tries = 0
    passCorrect = False
    passowrd = ""
    password2 = ""

    welcome()
    raw_input("***Caution***\nIf you forget your password you are about to create,\nyou will not be able to recover your phone code...\nPress [Enter] to continue")

    while(not passCorrect and tries < 3):
        password = raw_input("Enter your password to encrypt\n-->")
        password2 = raw_input("Enter your password again\n-->")
        tries += 1
        if password == password2:
            passCorrect = True
        elif tries < 2:
            print "Sorry, Try again..."

    if passCorrect:
        passwordHash = encryption.hash256(password)
        print "Your new code is\n-->",
  
        codeFile = open(".codes.txt")
        personalFile = open(".passcodes.txt", "w")
        
        random.seed(int(str(datetime.datetime.now().time())[9:]))

        randNum = random.randint(0, 10 ** 6)

        num = ""

        #iterates through the input file to find the new passcode
        for code in range(0, randNum + 1):
   	        num = codeFile.readline()
   	        if code == randNum:
                    print num
        codeFile.close()

        #goes to length - 1 because of the new line '\n' character at the end
        newNum = num[:len(num) - 1]

        cipher = encryption.AESCipher(passwordHash)
        encrypted = cipher.encrypt(newNum)

        personalFile.write(encrypted)
        personalFile.close()
  
        print "Password Completed..."
        print "In order to make this more secure, EXIT this current bash shell..."
    else:
        print "Password limit reached\nExiting..."
elif menuOption == 2:
    welcome()
    passcodes = open(".passcodes.txt", "r")
    
    encrypted = passcodes.read()
    
    password = raw_input("Please enter your password\n-->")
    passwordHash = encryption.hash256(password)

    cipher = encryption.AESCipher(passwordHash)
    decrypted = cipher.decrypt(encrypted)
    
    passcodes.close()

    print decrypted
else:
    print "Not a valid menu option..."
