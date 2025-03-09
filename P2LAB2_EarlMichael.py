# Michael Earl
# 03/9/25
# P2LAB2

print('this program takes the car you choose, outputs the MPG, and calulates the gas needed for the miles you input\n')

cars_and_mpg = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

keys = cars_and_mpg.keys()

print(keys)

car_choice = input('\nEnter a vehicle to see it\'s mpg: ')

if car_choice in cars_and_mpg:
    MPG = cars_and_mpg[car_choice]

    print(f'\nThe {car_choice} gets {MPG} mpg.  ')

    Miles = float(input(f'\nHow many miles will you drive the {car_choice}? '))

    Gas_needed = Miles / MPG

    print(f'\n{Gas_needed:.2f} gallon(s) of gas are needed to drive the {car_choice} {Miles} miles.')

else: 
    print('\nThe vehicle you entered is not in the dictionary')