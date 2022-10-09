
name = input("give me the names of your friends sprated by coma : ")
names = name.split(" , ")

from random import choice

paying = choice(names)
print(names)
print()
print(paying , "is going to pay")

