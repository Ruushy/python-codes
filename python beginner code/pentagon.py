from turtle import Turtle

t = Turtle()

def drwaing(num):
    angel = 360 / num
    for j in range(num):
        
        t.forward(100)
        t.right(angel)



for i in range(3 , 11):
    drwaing(i)


