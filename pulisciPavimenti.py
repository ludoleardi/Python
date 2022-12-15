# ogni secondo si muove in una direzione a caso di un cm, per due ore

import turtle
import random
import time

PIX = 10
schermo = turtle.Screen()
robot = turtle.Turtle()

robot.speed(2000)
while(True):
    dir = random.randint(0, 4)
    if(dir == 0):
        robot.forward(PIX)
    elif(dir == 1):
        robot.left(90)
        robot.forward(PIX)
        robot.right(90)
    elif(dir == 3):
        robot.backward(PIX)
    elif(dir == 4):
        robot.right(90)
        robot.forward(PIX)
        robot.left(90)
    #time.sleep(0.5)
    