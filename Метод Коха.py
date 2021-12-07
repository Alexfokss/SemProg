import random
from turtle import *
def kokh(_len,n):
    if n  == 0:
        pencolor(randint (0, 255), randint(0, 255), randint(0, 255))
        fd(_len)
    else:
        kokh(_len//3, n - 1)
        left(60)
        kokh(_len//3, n - 1)
        right(120)
        kokh(_len//3, n - 1)
        left(60)
        kokh(_len//3, n - 1)


colormode(255)
pensize(3)
up()
goto(-400, -200)
down()
kokh(300, 3)
exitonclick()