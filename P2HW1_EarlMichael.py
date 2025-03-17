# Michael Earl
# 3/5/25
# P1HW2

print('This Program will calculate and display your travel expenses...\n')

# main body of inputs 

budget = float(input('Enter your budget: '))


travel_dest = input('\nEnter your travel destination: ')


gas_cost = float(input('\nHow Much will you be spending on gas? '))


accommodation_cost = float(input('\nHow much will you be spending on accommodation/hotel? '))


food_cost = float(input('\nHow much will you be spending on food? '))


#total expenses 

total_expenses = gas_cost + accommodation_cost + food_cost

# final total after all expenses are subtracted from the budget

final_total = budget - total_expenses

print('\n--------Travel Expenses--------')

print(f'Location:               {travel_dest}')
print(f'Initial Budget:         ${budget:,.2f}')
print(f'Fuel:                   ${gas_cost:,.2f}')
print(f'Accommodation/hotel:    ${accommodation_cost:,.2f}')
print(f'Food:                   ${food_cost:,.2f}')

print('-------------------------------\n')

print(f'Remaining Balance:      ${final_total:,.2f}')









