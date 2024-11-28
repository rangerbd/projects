import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []

computer = []

def starting(players):
    user_total = 0
    for n in range(2):
        a = random.choice(cards)
        user_total += a
        players.append(a)
    
    print(f"{players}'s current_score is {user_total}")
starting(user)
starting(computer)