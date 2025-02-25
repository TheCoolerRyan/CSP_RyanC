def info(income, amount, type):
    pertype = amount/income*100
    print(f"You spend ${amount:.2f} on {type} and that is {pertype:.0f}% of your income.")


print("Welcome to your personal financial calculator that will help you realize how you spend your money.")

def user(type):
    type = user
    float(input(f"How much money is used on {type}?"))
user("income")
user("groceries")
user("transportation")
user("utilities")
user("rent")
income = user("income (Type how much do you earn?)")
groceries = user("groceries") 
transportation = user("transportation") 
utilities = user("utilities")
rent = user("rent")
user("income")
user("groceries")
user("transportation")
user("utilities")
user("rent")

savings = income/10
total_spending = rent+utilities+groceries+transportation+savings
spending_money = income-rent-utilities-groceries-transportation-savings
percent_spending_money = spending_money/income*100
info(income, rent, "rent")
info(income, savings, "savings")
info(income, transportation, "transportation")
info(income, groceries, "groceries")
info(income, utilities, "utilities")
info(income, total_spending, "total_spending")
print(f"And you also currently have ${spending_money:.2f} of spending money which is {percent_spending_money}% of your income.\n")