from turtle import *

speed(-1)
shape('turtle')
colors = ['red','blue','brown','yellow','silver']

for i in range(5):
    begin_fill()
    color(colors[i])
    for j in range(2):
        forward(100)
        left(90)
        forward(200)
        left(90)
    pu()
    forward(100)
    pd()
    end_fill()

mainloop()
    
