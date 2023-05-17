import math

print()
print(' Radians to Degrees Converter')
print()

radians_degrees = [('radian', 'degrees')]

print('Type yes to continue with conversion')
print()

for unit_radian, unit_degree in radians_degrees:
    print(f'{unit_radian} to {unit_degree}')

conversion = input('Type yes here -->')
conversion_index = str(conversion)

unit_radian, unit_degree = radians_degrees[conversion_index]
print()
from_value = float(input(f' Enter {unit_radian} here -->'))
print()

if radians_degrees == 1:
    