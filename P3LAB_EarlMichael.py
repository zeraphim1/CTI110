# Michael Earl

# 3/24/25

# P3LAB

print('This program calculates a breakdown of money is the most  efficient way possible!\n')

change = float(input('Enter the amount of money as a float: $'))

# if statment at the start to immediately respond with no change if a value is less that or equal to 0 

# yes, you can make if statements inside if statements

if change <= 0.00:
    print('No Change')
else:

# change equals value inputed by user times 100 to convert it to an integer

    change = int(change * 100)

# 1. dividing change by the value amount to get the variable amount
# 2. change is be subtracted by the variable * 100 so it keeps a running total
    dollars = change // 100
    change = change - (dollars * 100)

    quarters = change // 25
    change = change - (quarters * 25)

    dimes = change // 10
    change = change - (dimes * 10)

    nickles = change // 5
    change = change - (nickles * 5)

    pennies = change 

# logic flow to make sure its Dollar or Dollars depending on the value for each variable

    if dollars > 0:
        if dollars == 1:
            print(f'{dollars} Dollar')
        else:
            print(f'{dollars} Dollars')
    if quarters > 0:
        if quarters == 1:
            print(f'{quarters} Quarter')    
        else:
            print(f'{quarters} Quarters')    
    if dimes > 0:
        if dimes == 1:
            print(f'{dimes} Dime')
        else:
            print(f'{dimes} Dimes')
    if nickles > 0:
        if nickles == 1:
            print(f'{nickles} Nickle')
        else:
            print(f'{nickles} Nickles')
    if pennies > 0:
        if pennies == 1:
            print(f'{pennies} Penny')
        else: 
            print(f'{pennies} Pennies')                        

