### Written by Jason-Silla ###
### https://github.com/Jason-Silla/JohnAI ###

from __future__ import unicode_literals
from random import randint
from random import seed

def encrypt(message):
    try:
        intSeed = randint(1, 243)
        seed(intSeed)
        intSeed = randint(300, 1000)
        messageAsList = list(message)
        del(message)
        for i in range(len(messageAsList)):
            messageAsList[i] = intSeed * ord(messageAsList[i])
            randomVar = randint(1,3)
            if randomVar == 2 or randomVar == 3:
                if (messageAsList[i] <= 0x10ffff) and not messageAsList[i] == 113: 
                    try:
                        messageAsList[i] = chr(messageAsList[i])
                    except UnicodeEncodeError:
                        pass
            messageAsList[i] = str(messageAsList[i]) + "q"
        del(i, randomVar)
        partB = str((69420*intSeed))
        del(intSeed)
        partBAsList = list(partB)
        del(partB)
        partB1 = ""
        partB2 = ""
        i=0
        length = len(partBAsList)
        for number in partBAsList:
            partB1 = partB1 + number
            i = i+1
            if i == 3:
                break
        del(number)
        for var in range(len(partBAsList)):
            partB2 = partB2 + partBAsList[var+3]
            if var + 4 == length:
                break
        del(var)
        partA = ""
        partB1 = chr(int(partB1))
        partB2 = chr(int(partB2))
        partBFinal = partB1 + partB2
        for word in messageAsList:
            partA = partA + word
        encryptedMessage = partA + "orks" + partBFinal
        del(partA, partB1, partB2, partBAsList, partBFinal, word, messageAsList, i, length)
        return encryptedMessage
    except Exception:
        print("An ERROR has occured.")
def decrypt(encrypted):
    try:
        encryptedAsList = encrypted.split("orks")
        del(encrypted)
        i=0
        intseed = []
        for letter in encryptedAsList[1]:
            intseed.append(str(ord(letter)))
            i = i + 1
        del(i, letter)
        integerSeed = int(intseed[0] + intseed[1])/69420
        del(intseed)
        encryptedM = encryptedAsList[0].split("q")
        del(encryptedAsList)
        encryptedM.pop()
        decryptedMessage = ""
        for number in encryptedM:
            characterB = False
            try:
                int(number)
            except ValueError:
                characterB = True
            if not characterB:
                num = int(number)/integerSeed
                character = chr(int(num))
                decryptedMessage = decryptedMessage.__add__(character)
            else:
                num = ord(number)/integerSeed
                character = chr(int(num))
                decryptedMessage = decryptedMessage.__add__(character)
        del(encryptedM, number, num, characterB, integerSeed, character)
        return decryptedMessage
    except Exception:
        print("An ERROR has occured.")