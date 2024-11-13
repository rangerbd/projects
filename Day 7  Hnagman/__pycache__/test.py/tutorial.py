import random

word_list = ["abc","ved","red"]

chosen_word = random.choice(word_list)
print(chosen_word)
lenghth = len(chosen_word)

guess = input("enter a word ; ").lower()
print(guess)