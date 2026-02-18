'''
Budget Splicer - Takes monthly budget and splices it into predetermined categories

Following is steps following for development:
Step 1: Use input() to ask for income 
Step 2: Convert that input from a string to a float
Step 3: Create variables for your percentages (e.g., needs = income * 0.5 or 50/30/20 rule)
Step 4: print() the results with clear labels.
Step 5: Look up how to use open("budget.txt", "w") to save those results to a file on your computer.
'''

#Function to prompt user for their income
def getIncome():
    while True:
        try: #Checks the input for a float
            inputIncome = input("What is your monthly income? (In $USD): ")
            return float(inputIncome)
        except: #Throws an error for any improper input, tries again
            print("Not an acceptable number, please try again.")

monthlyIncome = getIncome()

# Predetermined splits for the monthly budget will be as follows (50/30/20)
# 50% for needs
# 30% for investments/savings/debts
# 20% for wants

needs = monthlyIncome * .5
savings = monthlyIncome * .3
wants = monthlyIncome * .2

print(f"Needs: {needs}, Savings: {savings}, Wants: {wants}")