import random
print("Welcome to the number guessing game \nI'm thinking of guessing a number between 1 to 100")
numbers =[]
for n in range(1,101):
    numbers.append(n)

selected_number = random.choice(numbers)
print(selected_number)
def easy_level(level):
    global attempt

    def difficulty_level():
        global attempt
        print(f"you have {attempt} attempt left")
        while attempt != 0:
            user_input = int(input("enter a number : "))
            if user_input == selected_number:
                print("you have guessed the correct number")
                break
            elif user_input != selected_number and user_input > selected_number:
                print("your guess is high")
                attempt -= 1
                print(f"you have {attempt} left")
            elif user_input != selected_number and user_input <selected_number:
                print("your guess is low")
                attempt -= 1
                print(f"you have {attempt} left")

        if attempt == 0 :
            print("you have used all the chances , you lose")

    if level == "easy":
        attempt = 10
        difficulty_level()
    else:
        attempt = 5
        difficulty_level()

level = input("easy or diffucult : ")

easy_level(level)

