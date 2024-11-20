customers_opinion = True
dictionaries = {}
while customers_opinion :
    name  = input("enter your name : ")
    money = int(input("how much you want to pay :"))

    dictionaries[name] = money

    option = input("is there any other bidder? yes or no")
    
    if option == "no":
        customers_opinion = False 

highest_score = 0
highest_bidder = ""
for letter in dictionaries:
    score = 0
    if dictionaries[letter] > score:
        score += dictionaries[letter]
        if score > highest_score:
            highest_score = score
            highest_bidder = letter
    
print(f"the winner is {highest_bidder} with a bid of {dictionaries[letter]}")

