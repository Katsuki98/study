from turtle import *

def draw_star(x,y,l):

    color('red')
    setx(x)
    sety(y)
    left(108)
    for i in range(5):
        forward(l)
        left(144)

draw_star(0,0,100)
mainloop()

