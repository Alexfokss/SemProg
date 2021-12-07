import turtle 
a = int(input())
b = 10

turtle.shape("turtle")

turtle.forward(100)

while a > 0:
    for i in range(a):
        turtle.circle(b*i)
        a = a - 1

turtle.exitonclick()