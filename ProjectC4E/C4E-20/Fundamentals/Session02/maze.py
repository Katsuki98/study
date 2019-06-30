from turtle import *

speed(-1)
shape('turtle')
color('black')

length = 5
# quang duong forward trong moi vong lap

for i in range(80):
    forward(length)
    left(90)
    length += 5
    # gan gia tri moi cho bien length
    # or: length = length + 5

mainloop()
