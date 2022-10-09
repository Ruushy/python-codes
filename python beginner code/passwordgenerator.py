import random

letter = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' ,
          'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
symbol = '><:"{}_)(*&^%$#@!'
number = "1234567890"


u_letter = int(input("how many letters do you want:? "))
u_symbol = int(input("how many symbol you want:? "))
u_number = int(input("how many numbers you want:? "))

passwrod = ""

for char in range(0 , u_letter):
    passw= random.choice(letter)

    passwrod += passw

for sy in range(0 , u_symbol):
    passwo = random.choice(symbol)
    passwrod+= passwo

for num in  range(0 , u_number):
    passwor = random.choice(number)
    passwrod += passwor

print("here's your password " , passwrod)
    
