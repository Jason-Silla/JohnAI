### Written by Jason-Silla ###
### https://github.com/Jason-Silla/JohnAI ###

from decimal import DivisionByZero
from random import randint
from math import sqrt

def factorialFinder(z):
    if z == 1:
        return 1
    else:
        return z*factorialFinder(z-1)

while True:
    print("""Which type of math would you like to do?
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Averager
6. Random Number Generator
7. Exponent
8. Exponential Graph
9. Area Calculator
10. Volume Calculator
11. Factorial Finder
12. Square Root Finder""")
    type = int(input("Please type the number before the type: "))

    while type > 12:
        type = int(input("Please enter a valid type: "))

    if type == 1:
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
        print(f"The sum is equal to {num1+num2}.")
        del(num1, num2)
    elif type == 2:
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
        print(f"The difference is equal to {num1-num2}.")
        del(num1, num2)
    elif type == 3:
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
        print(f"The product is equal to {num1*num2}.")
        del(num1, num2)
    elif type == 4:
        while True:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
            try:
                print(f"The sum is quotient to {num1/num2}.")
                break
            except ZeroDivisionError or DivisionByZero:
                print("You can't divide by 0.")
        del(num1, num2)
    elif type == 5:
        amountOfNumbers = 0
        total = 0
        print("Please enter the numbers you would like to average or average to get the average:")
        while True:
            temp = input()
            if temp == "average":
                break
            try:
                temp = int(temp)
                total += temp
                amountOfNumbers += 1
            except ValueError:
                print("Sorry, the value you entered was not a number or average. Please try again.")
        del(temp)
        print(f"The average is {total/amountOfNumbers}.")
        del(amountOfNumbers, total)
    elif type == 6:
        amount = int(input("How many random numbers would you like: "))
        size = int(input("What's the range you want these numbers to be in (min,max; default is 0-∞. To skip just click enter): "))
        size = size.split(",")
        if len(size):
            for i in range(amount):
                print(randint(0, 1000000000000000000))
            del(i)
        else:
            for i in range(amount):
                print(randint(size[0], size[1]))
            del(i)
        del(amount, size)
    elif type == 7:
        number = int(input("Please enter the whole number: "))
        expo = input("Please enter the exponent: ")
        normal = "0123456789"
        super_s = "⁰¹²³⁴⁵⁶⁷⁸⁹"
        res = expo.maketrans(''.join(normal), ''.join(super_s))
        expostr = expo.translate(res)
        print(f"{number}{expostr} is equal to {pow(number, int(expo))}.")
        del(number, expo, normal, super_s, res, expostr)
    elif type == 8:
        start = int(input("Please enter the starting value: "))
        expo = int(input("Please enter the exponent, or how much your graph will grow every time: "))
        length = int(input("Please enter how long you want the graph to be: "))
        print("1 ------>", start)
        old_total = start
        for i in range(length):
            total = pow(old_total, expo)
            old_total = total
            print(i+2, "------>", total)
        del(start, expo, length, old_total, i)
    elif type == 9:
        print("Only enter the number and make sure that all of the numbers are in the same unit.")
        l = int(input("Please enter the length: "))
        w = int(input("Please enter the width: "))
        print(f"The area is {l*w} square units.")
        del(l, w)
    elif type == 10:
        print("Only enter the number and make sure that all of the numbers are in the same unit.")
        l = int(input("Please enter the length: "))
        w = int(input("Please enter the width: "))
        h = int(input("Please enter the height: "))
        print(f"The volume is {l*w*h} cubed units.")
        del(l, w, h)
    elif type == 11:
        z = int(input("Please enter a whole number greater than 0: "))
        while z > 16:
            z = int(input("Please enter a whole number greater than 0: "))
        print(factorialFinder(z))
        del(z)
    elif type == 12:
        num = int(input("Please enter the number you'd like to find the square root of: "))
        print(f"The square root of {num} is {sqrt(num)}.")
        del(num)
    
    restartCalculator = input("Would you like to make another calculation (Y or N): ")
    if isinstance(restartCalculator, str):
        if restartCalculator.lower() == "y":
            pass
        else:
            break
    else:
        break
