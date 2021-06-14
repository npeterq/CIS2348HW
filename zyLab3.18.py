"Peter Nguyen"
"6/14/2021"
"CIS2348"
"1860823"
"3.18 LAB*: Program: Painting a wall"

height = float(input('Enter wall height (feet):\n'))
width = float(input('Enter wall width (feet):\n'))

area = height * width
paint = area / 350
cans = int(round(paint))

print('Wall area: ' + str(int(round(area))) + ' square feet')
print('Paint needed: {:.2f} gallons'.format(paint))
print('Cans needed: ' + str(cans) + ' can(s)')

color = input('\nChoose a color to paint the wall:\n')
if color == 'red':
    cost = 35 * cans
elif color == 'blue':
    cost = 25 * cans
elif color == 'green':
    cost = 23 * cans
else:
    cost = 0
print('Cost of purchasing ' + color + ' paint: $' + str(cost))

