import random
from hangman_art import stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for n in chosen_word:
    placeholder += "_"
print(placeholder)


game_over = False
correct_letter = []
lives = 6
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    if guess not in chosen_word:
        lives -=1
        print(stages[lives-1])
        if lives == 0:
            print("you,lose")
            break
    print(lives) 
   
    for letter in chosen_word:
        if letter == guess:
            display +=letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    
    
    print(display)

    if "_" not in display:
        game_over = True
        print("you win")
    elif lives == 0:
        print("you lose")