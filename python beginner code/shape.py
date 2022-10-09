from turtle import Turtle

t = Turtle()
t.speed(100)

for i in range(100):
    t.circle(100)
    t.setheading(t.heading() + 10)
    
