# Michael earl
# 3/5/25

print('This program is designed to calculate your monthly expenses and savings!\n')

print('If there is an expense you do not have just type 0(zero) and hit enter\n')


# main body of inputs

monthly_income = float(input('What is your monthly income? '))

house_insurance = float(input('\nWhat is your monthly renters/housing insurance? '))

house_expense = float(input('\nWhat is your monthly rent/mortgage? '))

utilities_expense = float(input('\nWhat is your monthly utility bill? '))


house_additional = float(input('\nWhat are your other monthly housing expenses? '))


car_payment = float(input('\nWhat is your monthly car payment? '))

car_insurance = float(input('\nWhat is your monthly car insurance bill? '))


car_gas = float(input('\nWhat is a rough estimate of your monthly gas expense? '))


car_additional = float(input('\nWhat are your other monthly car expenses? '))


grocieries_expense = float(input('\nWhat is monthly grocery cost? '))


eating_out = float(input('\nRoughly how much to you spend on eating out monthly? '))


other_expense = float(input('\nWhat are your other/miscellaneous expenses? '))


# final total by category

house_total = house_additional + house_expense + house_insurance + utilities_expense

car_total = car_additional + car_gas + car_insurance + car_payment

food_total = grocieries_expense + eating_out

# final expense

final_expense = house_total + car_total + food_total + other_expense

#expenses and stuff broken down

print('\n--------This is your monthly expenses broken down--------\n')

print(f'Monthly Income: ${monthly_income:.2f}')


print(f'Housing: ${house_total:.2f}')
print(f'Car: ${car_total:.2f}')
print(f'Food: ${food_total:.2f}')
print(f'Other/Miscellaneous: ${other_expense:.2f}\n')



print(f'Total Expenses: ${final_expense:.2f}\n')

final_total_expenses = monthly_income - final_expense

print(f'Monthly net gain/loss: ${final_total_expenses:.2f}\n')

#savings and investing reality

print('--------This is your monthly savings and investing reality based off your income--------\n')

living_expenses_reality = final_total_expenses * .8
investing_reality = final_total_expenses * .15
savings_reality = final_total_expenses * .05
 
 # hello

print(f'living expense: ${final_total_expenses:.2f}')
print(f'Investing: ${investing_reality:.2f}')
print(f'Emergency Fund: ${savings_reality:.2f}\n')

#savings and investing section recommendation

print('--------This is your monthly savings and investing recommendation based off your income--------\n')

living_expenses_recommend = monthly_income * .8 
investing_recommend = monthly_income * .15
savings_recommend = monthly_income * .05

print(f'living expenses: ${living_expenses_recommend:.2f}')
print(f'investing: ${investing_recommend:.2f}')
print(f'Emergency Fund: ${savings_recommend:.2f}')

input('Press Enter to exit...')