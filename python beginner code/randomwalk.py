from turtle import Turtle
import random


t = Turtle()

color = ["yellow" , "gold" , " maroon " , " turquoise" , " chocolate" ]
dirc = [0 , 90 , 180 , 270]
t.pensize(12)
t.speed(90)

for i in range(2000):
    #t.color(random.choice(color))
    t.forward(15)
    t.setheading(random.choice(dirc))
