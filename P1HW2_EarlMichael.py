# Michael Earl
# 3/5/25
# P1HW2

print('This Program will calculate and display your travel expenses...\n')

# main body of inputs 

budget = int(input('Enter your budget: '))
print()

travel_dest = input('Enter your travel destination: ')
print()

gas_cost = int(input('How Much will you be spending on gas? '))
print()

accommodation_cost = int(input('How much will you be spending on accommodation/hotel? '))
print()

food_cost = int(input('How much will you be spending on food? '))
print()

#total expenses 

total_expenses = gas_cost + accommodation_cost + food_cost

# final total after all expenses are subtracted from the budget

final_total = budget - total_expenses

print()
print('--------Travel Expenses--------')

print('Location:', travel_dest)
print('Initial Budget:', budget,)
print()

print('Fuel:', gas_cost)
print('Accommodation/hotel:', accommodation_cost)
print('Food:', food_cost)
print()

print('Remaining Balance:', final_total)







