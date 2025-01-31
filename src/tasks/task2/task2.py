from turtle import *
from random import randint
3
def middleware(level_of_recursion:int, size=300):
    Screen()  
    Turtle()  
    setheading(90) 
    speed(0)    
    pythagoras_branch(levels=level_of_recursion,trunkLen=90,angle=45,shrinkFactor=0.6)  
    exitonclick()

def pythagoras_branch(levels, trunkLen, angle, shrinkFactor):
    if levels!=0:
        color("red")
        forward(trunkLen)
        right(angle)
        pythagoras_branch(levels-1, trunkLen*0.7, angle, shrinkFactor)
        left(90)
        pythagoras_branch(levels-1, trunkLen*0.7, angle, shrinkFactor)
        right(angle)
        backward(trunkLen)
    
print("Write level of recursion:")
x=input()
if x.isnumeric():
    middleware(int(x))
else:print("Not a number!")