
#word_list = ['ardvark','baboon','camel']
import random
from hangman_word import word_list
from hagman_art import stage
lent = len(word_list)
ran = random.randint(0,lent-1)
lives = 6
place = 0
##chosen_word1 = word_list[ran]
chosen_word = random.choice(word_list)
##print(chosen_word1)
#gprint(chosen_word)
display = []
for char in chosen_word :
    display += "_"
#print(display)
condition = False
while not condition:
    guess = input("Guess a letter : ").lower()
    if guess in display :
        print(f"sorry you have guessed {guess}")
    for position in range(len(chosen_word)) :
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    if guess not in chosen_word:
        print(f"sorry {guess} not in the mistry word")
        lives -=1
        place +=1
        print(stage[place])
        if lives == 0:
            condition = True
            print("you lose")
    print(f"{''.join(display)}")
    if "_" not in display:
        condition = True
        print("you win")
    
print(f"the choosen word was {chosen_word}")