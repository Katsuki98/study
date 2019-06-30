from turtle import *
shape('turtle')
color('red')

n = int(input('Number of side: '))

for i in range(n):
    forward(100)
    left(360/n)
    
mainloop()