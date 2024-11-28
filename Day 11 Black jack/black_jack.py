import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
person_1 = []
computer = []
current_score = 0
total_computer = 0
user_choice = True


for number in range(2):
    random_selection = random.choice(cards)
    person_1.append(random_selection)
print(person_1)
for n in person_1:
    current_score += n 
print(f"total addition of userpoint is  {current_score}")
if current_score == 21:
    print("you win")
    
elif current_score > 21:
    print("busted")
    print("you lose")
else:

    while user_choice:
        choice  = input("would to like to add another card: press Y for yes and N for No: ").lower()
        if choice ==  "y":
            random_selection = random.choice(cards)
            print(random_selection)
            current_score += random_selection
            print(current_score)
            break
        else:
            user_choice = False
        


    


    



