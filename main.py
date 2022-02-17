### Written by Jason-Silla ###
### https://github.com/Jason-Silla/JohnAI ###

from User import User, Month
from os.path import exists, join
from platform import system as os
from os import system
from os import remove
from random import randint
from datetime import datetime
import hide
import sys

try:
    ### Generalized Words ###
    greetings = ["hello", "hi", "yo"]
    adioses = ["bye", "adios", "goodbye", "leave"]
    yes = ["ya", "yes", "sure", "definetly", "def", "obv", "obviously"]

    user = User()
    ### New User ###
    if not exists("user.txt"):
        loop = True
        loop2 = True
        while loop:
            while True:
                letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
                username = input("Enter a username: ")
                username.strip()
                usernameLower = username.lower()
                for character in usernameLower:
                    for letter in letters:
                        if character == letter:
                            loop2 = False
                            break
                    if not loop2:
                        break
                if loop2:
                    print("Your username must have at least 1 character.")
                del(usernameLower, character, letter, loop2)
                else:
                    break
            ### Make file ###
            newuser = open("user.txt", "w")
            newuser.write(hide.encrypt(username) + '\n')
            ### Add user infomation to list ###
            userinfo = [username]
            del(username)
            user.setUserInfo(userinfo)
            del(userinfo)
            lineCount = 0
            newuser.close()
            newuser = open("user.txt", "r")
            ### Make sure username is added to file ###
            for line in newuser:
                if line != "\n":
                    lineCount += 1
                    if lineCount != 1:
                        print("An error occured. Please try again.")
                        remove("user.txt")
                    elif lineCount == 1:
                        print("Successfully created a new user.")
                        loop = False
            del(line, lineCount)
            newuser.close()
        del(loop)
        ### Returning User ###
    elif exists("user.txt"):
        returninguser = open("user.txt", "r")
        userinfo = []
        ### Get information from file ###
        for line in returninguser:
            userinfo.append(str(hide.decrypt(line)))
        for i in range(len(userinfo)):
            userinfo[i] = (userinfo[i])[:len(userinfo[i])-1]
            user.setUserInfo(userinfo)
            if user.username == "":
                loop2 = True
                while True:
                letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
                username = input("AN ERROR OCCURED IN YOUR FILE. PLEASE REENTER YOUR USERNAME: ")
                username.strip()
                usernameLower = username.lower()
                for character in usernameLower:
                    for letter in letters:
                        if character == letter:
                            loop2 = False
                            break
                    if not loop2:
                        break
                if loop2:
                    print("Your username must have at least 1 character.")
                del(usernameLower, character, letter, loop2)
                else:
                    user.setUsername(username)
                    user.userFileReset()
                    break
            returninguser.close()
        del(userinfo, line, i)

    ### Variables ###
    attempts = 0
    response = ""
    responseByWord = []

    ### Main AI Loop ###
    while True:
        ### Get request ###
        response = input()
        ### Convert reponse to list ###
        responseByWord = response.lower().split(" ")
        ### Check for specfic requests ###
        if response == "exit" or response == "quit":
            exit()
        ### Clears Screen ###
        elif response == "clear" or response == "cls":
            if os() == "Darwin" or os() == "Linux" or os() == "Java":
                system("clear")
            elif os() == "Windows":
                system("CLS")
        ### Sets Birthday ###
        elif response == "set birthday":
            birthday = input("Enter your birhtday (12/25/1984): ")
            birthdayAsList = birthday.split("/")
            user.setBirthday(birthdayAsList[0], birthdayAsList[1], birthdayAsList[2])
        else:
            ### Loops through each word to find key words ###
            for word in responseByWord:
                ### Makes the user look like a hacker ###
                if word == "hacker":
                    for i in range(5000000):
                        print(randint(1,100000000), end="")
                    print()
                    break
                ### This is for if the user is buying a PC ###
                elif word == "pc":
                    ### Finds file ###
                    if exists(f"accounts/{user.userFile}"):
                        userfile = open(f"accounts/{user.userFile}", "r+")
                        ### Gets amount of money if unavailable ###
                        if user.pcMoney <= -1:
                            while True:
                                user.pcMoney = int(input("Please enter how much your PC costs: "))
                                if user.pcMoney < 0:
                                    print("Amount of money for PC must be greater than 0.")
                                else:
                                    break
                            ### Adds amount of money to file ###
                            userfile.write(user.userFileReset())
                        else:
                            ### Prints amount of money for PC if available ###
                            print(f"You need ${user.pcMoney} more to buy the PC you want.")
                    break
                ### Opens applications ###
                elif word == "open":
                    pass
                    break
                ### Prints date and time ###
                elif word == "time" or word == "date":
                    now = datetime.now()
                    month = Month(datetime.today().month)
                    print(f"Today is {str(month)[-3:]} {datetime.today().day}, {datetime.today().year} and it is {now.strftime('%H:%M:%S')}")
                    break
                ### Runs the calculator ###
                elif word == "calculator":
                    system("python3 calculator.py")
                    break
                else:
                    ### Checks to see if the user said a greeting ###
                    for greeting in greetings:
                        if greeting == word:
                            print(f"Hi {user.firstName}! I'm John, your AI Assistant.")
                            break
                    ### Checks to see if the user said an adios ###
                    for adios in adioses:
                        if adios == word:
                            print(f"Have a nice day {user.firstName}")
                            exit()
                    ### Interpreting Statements Testing ###
                    if len(responseByWord) < 6:
                        requiredWords1 = ["what", "can", "you", "do"]
                        requiredAmount = 0
                        doB = False
                        for requiredWord in requiredWords1:
                            if requiredWord == word:
                                requiredAmount += 1
                                if word == "do":
                                    doB = True
                                if requiredAmount >= 3 and doB:
                                    print("""I can do:
- Complex Algebraic Equations
- Basic Math through an Installed calculator
- Make you look like a hacker
- Tell you the date and time""")
                                

        ### Empty the response list ###
        responseByWord.clear()
except Exception as error:
    print("AN ERROR HAS OCCURED SOMEONE IN THE PROGRAM!!! PLEASE REPORT THE ERROR AT https://github.com/Jason-Silla/JohnAI")
    print(error)
    exception_type, exception_object, exception_traceback = sys.exc_info()
    del(exception_type)
    filename = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno
    print("File name: ", filename)
    print("Line number: ", line_number)
