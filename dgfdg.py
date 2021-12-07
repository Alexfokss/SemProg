import turtle 

a, n =  map(int,input().split())
def kokh(a, n):
    if n == 0:
        turtle.forward(a)
    else:
        kokh(a//3, n - 1)
        turtle.left(60)
        kokh(a//3, n - 1)
        turtle.right(120)
        kokh(a//3, n - 1)
        turtle.left(60)
        kokh(a//3, n - 1)


turtle.shape("turtle")


for i in range(n):
    kokh(300, 3)
    turtle.right(120)


turtle.exitonclick()
# turtle.pencolor (random.randint(0, 255), (random.randint(0, 255))