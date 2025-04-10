# Ryan Crop, Financial calculator python
print("This calculator will help you deal with Finances.\n")
def info(income, amount,type):
    pertype = (amount/income)*100
    print(f"You spend ${amount:.2f} on {type} and that is {pertype:.0f}% of your income.")

def questions(inputs):
    questions = float(input(f"What is your monthly {inputs}?\n"))
   
    return questions

income= float(input ("what is your monthly income?\n"))
rent = float(input ("what is your monthly rent cost?\n"))
utilities = float(input ("what is your monthly utilities cost?\n"))
groceries = float(input ("what is your monthly grocery cost?\n"))
transport = float(input ("what is your monthly transport cost?\n"))
savings = float(income/10)
expenses = float(rent+utilities+groceries+transport+savings)
spending = float(income-expenses)

info(income, rent, "rent")
info(income, utilities, "utilities")
info(income, transport, "transport")
info(income, savings, "savings")
info(income, expenses, "expenses")
info(income, spending, "spending (What you have left to use on whatever you want.)")
info(income, groceries, "groceries")