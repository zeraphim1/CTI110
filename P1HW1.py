# Michael Earl
# 3/5/25
# P1HW1
# I created this script for simple calulations

# section 1, exponenet calulations 

print('----Calculating Exponenets-----\n')

base_value = int(input('Enter an integer as a base value: '))

exponenet = int(input('Enter an integer as the exponent: '))
print()

equation_1 = base_value ** exponenet 

# outcome 1 below

print(base_value, 'raised to the power of', exponenet, 'is', equation_1, "!!\n")

#section 2 , addition and subtraction

print('----Addition and subtraction----\n')

starting_integer = int(input('Enter a starting integer: '))

adding_integer = int(input('Enter an integer to add: '))

subtracting_integer = int(input('Enter an integer to subtract: '))
print()

equation_2 = starting_integer + adding_integer - subtracting_integer

#outcome 2 below

print(starting_integer, '+', adding_integer, '-', subtracting_integer, 'is equal to', equation_2 )

