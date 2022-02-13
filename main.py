### Written by Jason-Silla ###
### https://github.com/Jason-Silla/JohnAI ###

from User import User, Month
from os.path import exists, join
from platform import system as os
from os import system as sys
from os import remove
from random import randint
from datetime import datetime
import hide

try:
    ### Generalized Words ###
    greetings = ["hello", "hi", "yo"]

    user = User()
    ### New User ###
    if not exists("user.txt"):
        loop = True
        while loop:
            username = input("Enter a username: ")
            ### Make file ###
            newuser = open("user.txt", "w")
            newuser.write(hide.encrypt(username) + '\n')
            ### Add user infomation to list ###
            userinfo = [username]
            user.setUserInfo(userinfo)
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
            returninguser.close()

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
                sys("clear")
            elif os() == "Windows":
                sys("CLS")
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
                    sys("python3 calculator.py")
                    break
                else:
                    ### Checks to see if the user said a greeting ###
                    for greeting in greetings:
                        if greeting == word:
                            print(f"Hi {user.firstName}! I'm John, your AI Assistant.")
                            break

        ### Empty the response list ###
        responseByWord.clear()
except Exception as error:
    print("AN ERROR HAS OCCURED SOMEONE IN THE PROGRAM!!! PLEASE REPORT THE ERROR AT https://github.com/Jason-Silla/JohnAI")
    print(error)
