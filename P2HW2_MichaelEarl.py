# Michael Earl

# 3/17/25

# P2HW2

print('This program calculates average test scores\n')

mod_1 = float(input('Enter grade for Module 1: '))

mod_2 = float(input('Enter grade for Module 2: '))

mod_3 = float(input('Enter grade for Module 3: '))

mod_4 = float(input('Enter grade for Module 4: '))

mod_5 = float(input('Enter grade for Module 5: '))

mod_6 = float(input('Enter grade for Module 6: '))

# creating a list from input varibles below

all_mods = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

min_grade = min(all_mods)

high_grade = max(all_mods)

sum_grade = sum(all_mods)

len_mods = len(all_mods)

avg_grade = sum_grade/len_mods

# Displaying output in a clean vertical column

print('\n------------Results------------')

print(f'lowest Grade:       {min_grade:.2f}')
print(f'Highest Grade:      {high_grade:.2f}')
print(f'Sum of Grades:      {sum_grade:.2f}')
print(f'Average:            {avg_grade:.2f}')

print('-------------------------------')

