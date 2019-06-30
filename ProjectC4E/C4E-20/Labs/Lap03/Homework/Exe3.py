from turtle import *

def draw_square(l,c):
    color(c)
    for i in range(4):
        forward(l)
        left(90)

draw_square(100,'red')
mainloop()




