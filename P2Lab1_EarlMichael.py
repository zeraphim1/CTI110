# Michael Earl
# 03/9/25
# P2LAB1

print('This project calculates diffrent values of a circle!')

# I probaly dont even need to be importing math becasue I specified PI, but it can't hurt

import math

PI =  3.14159

Radius = float(input(f'\nWhat is the radius of the circle? '))

Diameter = 2 * Radius

print(f'\nThe diameter of the circle is {Diameter:.1f}')

Circumference = (2 * PI) * Radius

print(f'\nThe circumference of the circle is {Circumference:.2f}')

Area = PI * (Radius ** 2)

print(f'\nThe area of the circle is {Area:.3f}')