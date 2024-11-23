def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2

dic = {"+": add,
       "-":sub,
       "*":mul,
       "/":div,
       }
user_choice = True
number_1 = int(input("enter the first number: - "))
calculation = 0
while user_choice:
    for operators in dic:
        print(operators)
    operations = input("enter the operator : ")
    number_2 = int(input("enter the second number: - "))
    calculation = dic[operations](number_1,number_2)
    print(calculation)





    choice = input(f"do you want to keep calculating with {calculation}  yes or no : ")
    if choice == "no":
        user_choice = False
    else:
        number_1 = calculation