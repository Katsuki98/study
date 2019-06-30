from turtle import *

speed(-1)
shape('turtle')
colors = ['red','blue','brown','yellow','grey']

for j in range(3,8):
    color(colors[j-3])
    for i in range(j):
        forward(100)
        left(360/j)

mainloop()