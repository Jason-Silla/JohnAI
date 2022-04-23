# Import Necessary Modules
from random import randint
from time import sleep
import cv2
import numpy

def setVariables():
    global dead
    dead = False
    global goingRight 
    goingRight = False
    global goingLeft
    goingLeft = True
    global goingUp
    goingUp = False
    global goingDown
    goingDown = False
    global eating
    eating = True
    global deathBySelf
    deathBySelf = False
    global foodx
    foodx = 0
    global foody
    foody = 0
    global x
    x = 300
    global y
    y = 150
    global snake
    snake = 3
    global score
    score = 0
    global snakex
    snakex = [300]
    global snakey
    snakey = [150]

if __name__ == "__main__":
    # Make a blank screen for the game to go on
    blank = numpy.zeros((300, 500, 3), dtype="uint8")

    # Puts text on the center of the screen
    cv2.putText(blank, "Click Space to Start", (blank.shape[1]//2 - 200, blank.shape[0]//2), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("Snake", blank)

    # Waits until spacebar is pressed
    if cv2.waitKey(0) == 32:
        pass

    # Main Game Loop   
    while True:
        setVariables()
        # Clears the screen and puts 3
        cv2.rectangle(blank, (0, 0), (blank.shape[1], blank.shape[0]), (0, 0, 0), -1)
        cv2.putText(blank, "3", (blank.shape[1]//2, (blank.shape[0]//2)), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255), 4)
        cv2.imshow("Snake", blank)
        cv2.waitKey(1)
        sleep(1)

        # 2
        cv2.rectangle(blank, (0, 0), (blank.shape[1], blank.shape[0]), (0, 0, 0), -1)
        cv2.putText(blank, "2", (blank.shape[1]//2, (blank.shape[0]//2)), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255), 4)
        cv2.imshow("Snake", blank)
        cv2.waitKey(1)
        sleep(1)

        # 1
        cv2.rectangle(blank, (0, 0), (blank.shape[1], blank.shape[0]), (0, 0, 0), -1)
        cv2.putText(blank, "1", (blank.shape[1]//2, (blank.shape[0]//2)), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255), 4)
        cv2.imshow("Snake", blank)
        cv2.waitKey(1)
        sleep(1)

        # Clears the screen
        cv2.rectangle(blank, (0, 0), (blank.shape[1], blank.shape[0]), (0, 0, 0), -1)

        while not dead:
            good = False
            k = 0
            # Gets the direction you are going in
            direction = cv2.waitKey(1)
            if direction == 87 or direction == 119 and not goingDown:
                goingUp, goingDown, goingLeft, goingRight = True, False, False, False
            elif direction == 65 or direction == 97 and not goingRight:
                goingLeft, goingRight, goingUp, goingDown = True, False, False, False
            elif direction == 83 or direction == 115 and not goingUp:
                goingDown, goingUp, goingLeft, goingRight = True, False, False, False
            elif direction == 68 or direction == 100 and not goingLeft:
                goingRight, goingLeft, goingUp, goingDown = True, False, False, False
            
            # Changes your x/y depending on the direction you're going
            if goingRight:
                x += 10
            elif goingLeft:
                x -= 10
            elif goingUp:
                y -= 10
            elif goingDown:
                y += 10
            
            # Writes a red square at the x and y coordinates
            cv2.rectangle(blank, (x, y), (x+10, y+10), (0, 0, 255), -1)
            
            if snake == len(snakex):
                # Writes black square to cover up end square (no infinate snake)
                cv2.rectangle(blank, (snakex[snake-1], snakey[snake-1]), (snakex[snake-1]+10, snakey[snake-1]+10), (0, 0, 0), -1)
                # Removes last element from snakex and snakey and places new one at beginning
                snakex.pop()
                snakey.pop()
                snakex.insert(0, x)
                snakey.insert(0, y)
            else:
                # Adds new x and y at beginning
                snakex.insert(0, x)
                snakey.insert(0, y)
            
            # Generate new food
            if eating:
                while not good:
                    foodx = (randint(1, 29))*10
                    foody = (randint(1, 14))*10
                    # Makes sure food isn't on snake
                    while not len(snakex) == k:
                        if foodx == snakex[k] and foody == snakey[k]:
                            good = False
                            break
                        else:
                            good = True
                        k+=1
                eating = False
                # Draws food
                cv2.rectangle(blank, (foodx, foody), (foodx+10, foody+10), (0, 255, 0), -1)
            
            # Checks to see if food is eaten and changes snake
            if x == foodx and y == foody:
                snake+=2
                score+=1
                eating = True
            k = 1

            # Checks to see if snake ran into itself
            while len(snakex) > k and not dead:
                if x == snakex[k] and y == snakey[k]:
                    dead = True
                    deathBySelf = True
                k+=1
            
            # Checks to see if snake hit wall
            if x == 500 or y == 300 or x == 0 or y == 0:
                dead = True
            cv2.imshow("Snake", blank)
            sleep(0.25)

        # Changes k depending on how the snake died
        if deathBySelf:
            k = 1
        else:
            k = 0

        # Animates snake death
        while not len(snakex) == k:
            cv2.rectangle(blank, (snakex[k], snakey[k]), (snakex[k]+10, snakey[k]+10), (0, 0, 0), -1)
            k+=1
            cv2.waitKey(1)
            cv2.imshow("Snake", blank)
            sleep(0.1)
        
        # Removes last snake block
        cv2.rectangle(blank, (snakex[snake-1]+10, snakey[snake-1]+10), (snakex[snake-1]+20, snakey[snake-1]+20), (0, 0, 0), -1)
        cv2.imshow("Snake", blank)
        cv2.waitKey(1)

        # Displays score
        cv2.rectangle(blank, (0, 0), (blank.shape[1], blank.shape[0]), (0, 0, 0), -1)
        cv2.putText(blank, f"Score: {score}", ((blank.shape[1]//2)-170, (blank.shape[0]//2)), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 255, 255), 4)
        cv2.imshow("Snake", blank)

        # If space is pressed, play again; if q is pressed, exit
        while True:
            key = cv2.waitKey(1)
            if key == 32:
                break
            elif key == 81 or key == 113:
                exit()