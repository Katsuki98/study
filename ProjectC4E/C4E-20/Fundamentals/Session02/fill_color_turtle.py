from turtle import Turtle, Screen

my_size = 70
my_angle = 360 / 8

def drawPolygon(turtle, size, angle):
    """ Make 'turtle' draw a polygon of 'size' with 'angle' """

    for _ in range(int(360 / angle)):
        turtle.forward(size)
        turtle.left(angle)

wn = Screen()
wn.bgcolor("yellow")

yertle = Turtle()
yertle.color("white", "white")

yertle.begin_fill()
drawPolygon(yertle, my_size, my_angle)
yertle.end_fill()

wn.exitonclick()