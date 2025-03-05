# Michael earl
# 3/5/25

print('This program is designed to calculate your monthly expenses and savings!\n')

print('If there is an expense you do not have just type 0(zero) and hit enter')
print()

# main body of inputs

monthly_income = float(input('What is your monthly income? '))
print()

house_insurance = float(input('What is your monthly renters/housing insurance? '))
print()

house_expense = float(input('What is your monthly rent/mortgage? '))
print()

utilities_expense = float(input('What is your monthly utility bill? '))
print()

house_additional = float(input('What are your other monthly housing expenses? '))
print()

car_payment = float(input('What is your monthly car payment? '))
print()

car_insurance = float(input('What is your monthly car insurance bill? '))
print()

car_gas = float(input('What is a rough estimate of your monthly gas expense? '))
print()

car_additional = float(input('What are your other monthly car expenses? '))
print()

grocieries_expense = float(input('What is monthly grocery cost? '))
print()

eating_out = float(input('Roughly how much to you spend on eating out monthly? '))
print()

other_expense = float(input('What are your other/miscellaneous expenses? '))
print()

# final total by category

house_total = house_additional + house_expense + house_insurance + utilities_expense

car_total = car_additional + car_gas + car_insurance + car_payment

food_total = grocieries_expense + eating_out

# final expense

final_expense = house_additional + house_expense + house_insurance + utilities_expense + car_additional + car_gas + car_insurance + car_payment + grocieries_expense + eating_out + other_expense

#expenses and stuff broken down

print('--------This is your monthly expenses broken down--------\n')

print('Monthly Income:', monthly_income)


print('Housing:', house_total)
print('Car:', car_total)
print('Food:', food_total)
print('Other/Miscellaneous:', other_expense)
print()


print('Total Expenses:', final_expense)
print()

final_total_expenses = monthly_income - final_expense

print('Monthly net gain/loss:', final_total_expenses)
print()


#savings and investing reality

print('--------This is your monthly savings and investing reality based off your income--------\n')

living_expenses_reality = final_total_expenses * 8
investing_reality = final_total_expenses * .15
savings_reality = final_total_expenses * 2

print('living expense:', final_total_expenses)
print('Investing:', investing_reality)
print('Emergency Fund:', savings_reality)
print()

#savings and investing section recommendation

print('--------This is your monthly savings and investing recommendation based off your income--------\n')

living_expenses_recommend = monthly_income * .8 
investing_recommend = monthly_income * .15
savings_recommend = monthly_income * .05

print('living expenses:', living_expenses_recommend)
print('investing:', investing_recommend)
print('Emergency Fund', savings_recommend)

