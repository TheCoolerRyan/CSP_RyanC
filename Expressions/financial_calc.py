#Ryan Crop, Finaincal calculator.py

#Write a print statement telling the user what the program is (Bugdet calc) -

#Ask for monthley income -

#Ask for rent amount  -

# Ask for utilites -

#Ask for groceries -

#Ask for transportation -

# Calculate savings as 10% of income (Variable) -

#Calculate spending money  income - (rent + utilities + grocieries + transportations + savings) (Variable) -

#Calculate percent of rent (rent/income) -

#Calculate percent of utilites (utilites/income) -

#Calculate percent of grocieries (groceries/income) -

#Calculate percent of transportation (transportation/income)-

# Calculate percent of spending (spending/income)-

# tell user category spending amount and percent ("You spend $xx.xx on rent and that is xx% of your income") for all

print("Hello this is a finacial calculator to help you know how much you spend compared to income.")
income = float(input("How much money do you make each month?"))
print("Okay")

rent = float(input("How much did you spend on Rent?"))
utilites = float(input("Okay, how much did you spend on utilites?"))
grociries = float(input("Got it, so how much did you spend on grocies?"))
transportation = float(input("And finally how much did you spend on transportation?"))
savings = float(income/90)
spending_money = float(income - (rent+utilites+grociries+transportation+savings))
percent_rent = float(rent/income)
percent_utilites = float(utilites/income)
percent_grociries = float(grociries/income)
percent_transportation = float(transportation/income)
percent_spending_money = float(spending_money/income)
print("The amount you spend on rent is", rent) 
print("and the percent of your income you spend on rent is",percent_rent)
print("The amount you spend on grociries are", grociries) 
print("and the percent of your income you spend on grociries is",percent_grociries)
print("The amount you spend on utilities are", utilites) 
print("and the percent of your income you spend on utilities is",percent_utilites)
print("The amount you spend on transportation is", transportation) 
print("and the percent of your income you spend on transportation is",percent_transportation)
print("The amount of money you should save is",savings)
print("Finally the amount of spending money you have to use is",spending_money)