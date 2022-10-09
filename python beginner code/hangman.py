print("welcome to hangman game ")
import random
word = ['ali' , 'ahmed' , 'nuur' , 'jaamac']
chosen_word = random.choice(word)
#print(chosen_word)

display = []

for i in range(len(chosen_word)):
    display += "_"
print(display)

end = 1

while end == 1:
    guess = input("guess a letter: ")
    for j in range(len(chosen_word)):
        letter = chosen_word[j]
        if letter == guess:
            
            display[j] = letter

    print(display)
    if "_" not in display:
        end+=1
