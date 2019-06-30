from turtle import *

speed(-1)
shape('turtle')
color('blue')

for i in range(0,150,3):
    forward(i)
    left(90)
    forward(i)
    left(90)
    forward(i)
    left(90)
    forward(i)
    left(80)
    
mainloop()