# Michael Earl

# 3/31/25

# P3HW2

print('This program calculates employee pay\n')

name_employee = input('Enter employee\'s name: ')

hours_employee = float(input('Enter number of hours worked: '))

pay_employee = float(input('Enter employee\'s pay rate: '))

# calling variables to set up for if statement

regular_pay = 0

overtime_hours = 0

overtime_pay = 0

gross_pay = 0

# if statement below to deal with the over or under of 40 hours calculations

if hours_employee > 40:
    regular_pay = 40 * pay_employee  
    overtime_hours = hours_employee - 40  
    overtime_pay = overtime_hours * (pay_employee * 1.5)  
else:
    regular_pay = hours_employee * pay_employee  

gross_pay = regular_pay + overtime_pay

# print statements below, organized in a way that both rows will match regardless of input 

print('------------------------------------')
print(f'Employee name: {name_employee}\n')

print(f'{"Hours Worked":<15}{"Pay rate":<10}{"OverTime":<10}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay":<15}')
print('-------------------------------------------------------------------------------')
print(f'{hours_employee:<15}{pay_employee:<10}{overtime_hours:<10}{overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<15.2f}')