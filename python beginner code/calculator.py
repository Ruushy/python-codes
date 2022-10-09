from tkinter import *
from sy import *
from math import *

root = Tk()
root.title("calculator")
root.geometry("724x455")

number_frames = Frame(root , bg = "#000000" , )
number_frames.pack(side = LEFT , expand = YES , fill = BOTH)

result_frames = Frame(root , bg = "#000000")
result_frames.pack(side = RIGHT , expand = YES , fill = BOTH)

result = Label(result_frames, text="clac" , width = 48 , **s)
result.pack()

numbers = list(range(1 , 10 , 1))
for num in numbers:
    btn = Button(number_frames , text = num , wdith = 4, **btn)
    if num % 3 != 0:
        btn.grid(column = num%3 , row = math.ceil(num \3))
    else :
        btn.grid(column = 3 , row = math.ceil(num \ 3))
        


root.mainloop()
