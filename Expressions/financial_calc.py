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
percent_rent = float(rent/income)*100
percent_utilites = float(utilites/income)*100
percent_grociries = float(grociries/income)*100
percent_transportation = float(transportation/income)*100
percent_spending_money = float(spending_money/income)*100
print("The amount you spend on rent is", round(rent,2)) 
print("and the percent of your income you spend on rent is",round(percent_rent,2))
print("The amount you spend on grociries are", round(grociries,2)) 
print("and the percent of your income you spend on grociries is",round(percent_grociries,2))
print("The amount you spend on utilities are", round(utilites,2)) 
print("and the percent of your income you spend on utilities is",round(percent_utilites,2))
print("The amount you spend on transportation is", round(transportation,2)) 
print("and the percent of your income you spend on transportation is",round(percent_transportation,2))
print("The amount of money you should save is",round(savings,2))
print("Finally the amount of spending money you have to use is",round(spending_money,2))
print("Oh yeah, also the amount of percent that your spending money is",round(percent_spending_money,2))
# Make sure not to put more spent then earned
