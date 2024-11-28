import random
from game_data import data

wining_stack = True
total_score = 0
while wining_stack:
    a = random.choice(data)
    b = random.choice(data)

    def print_output(random_data):
        for n in random_data:
            if n != 'follower_count':
                print(f"{n} : {random_data[n]}")
            else:
                print(f"{n} : ***")
        
    print_output(a)
    print(f"VS")
    print_output(b)

    user_selection = input("Who's got more followers a or b : ")
    if user_selection == "a" and a['follower_count'] > b['follower_count']:
        print("you win")
        total_score += 1
    elif user_selection == "b" and b['follower_count'] > a['follower_count']:
        print("you win")
        total_score += 1
    else:
        print("you lose")
        print(f"your total score is {total_score}")
        wining_stack = False


