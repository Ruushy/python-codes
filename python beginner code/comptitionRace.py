import tkinter.messagebox
import turtle
import random
import time


screen = turtle.Screen()
screen.bgcolor('lightblue')

player_one = turtle.Turtle()
player_one.color("blue")
player_one.shape('turtle')


player_two = player_one.clone()
player_two.color('red')

player_one.penup()
player_one.goto(-300 , 200)

player_two.penup()
player_two.goto(-300 , -200)

player_one.goto(300 , -200)
player_one.left(90)
player_one.color('black')
player_one.pendown()
player_one.forward(400)
player_one.write("finish" , font=40)
player_one.penup()
player_one.right(90)
player_one.color("blue")
player_one.goto(-300,200)

die = [1 ,2 ,3 ,4,5,6]
player_one.pendown()
player_two.pendown()

for i in range(30):
    if player_one.pos() >= (300 , 200):
        tkinter.messagebox.showinfo("congtats" , "player Blue won the race")
        break
    elif player_two.pos() >= (300 , -200):
        tkinter.messagebox.showinfo("congtats" , "player Red won the race")
        break

    else:
        die_rol = random.choice(die)
        player_one.forward(30*die_rol)
        time.sleep(1)

        die_rol2 = random.choice(die)
        player_two.forward(30*die_rol2)
        time.sleep(1)
        
        
    









turtle.done()

