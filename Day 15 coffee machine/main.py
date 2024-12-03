from data import menu 
from data import resources
total_cost = 0
total_deposit = 0
return_money = 0
quarter = .25
penny = .01
dime = .10
nichel = .05

order = input("what would you like?(espresso , cappuchino, latte : )")
deposit_quarter = int(input("how many quarter: "))
deposit_penny = int(input("how many penny: "))
deposit_dime = int(input("how many dime: "))
deposit_nichel = int(input("how many nichel: "))

total_deposit = (deposit_penny * penny) + (deposit_quarter * quarter) + (deposit_dime * dime) + (deposit_nichel * nichel) 
print(f"total deposit is {total_deposit}")
#if the customer wants to show the remaining ingredients
user_choice = True

#find out cost according to order
while user_choice:
    for type in menu:
        if type == order:
            print(f"the price of the {order} is {menu[type]["cost"]}")
            total_cost += menu[type]["cost"]
            if total_cost < total_deposit:
                temporary = total_deposit - total_cost
                return_money += temporary



            #deduct ingredients from the resources
                for item in menu[order]:
                    print(item)

            

                    

        else:
            print("you dont have enough money . money is refunded")
            print(f"heres your change {return_money}")
            break


