import math
from turtle import *

def heart1(X):
    return 15*math.sin(X)**3

def heart2(X):
    return 12*math.cos(X)-5*\
    math.cos(2*X)-2*\
    math.cos(3*X)-\
    math.cos(4*X)
speed(0)
bgcolor("blacK")
for i in range(600):
    goto(heart1(i)*20,heart2(i)*20)
    for j in range(5):
        color("red")
    goto(0,0)
done()