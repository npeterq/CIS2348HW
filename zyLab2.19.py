"Peter Nguyen"
"6/14/2021"
"CIS2348"
"1860823"
"2.19 CIS 2348 LAB*: Program: Cooking measurement converter"

lemon = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
nectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields {:.2f} servings'.format(servings))
print('{:.2f} cup(s) lemon juice'.format(lemon))
print('{:.2f} cup(s) water'.format(water))
print('{:.2f} cup(s) agave nectar'.format(nectar))

servings_required = float(input('\nHow many servings would you like to make?\n'))

print('\nLemonade ingredients - yields {:.2f} servings'.format(servings_required))
print('{:.2f} cup(s) lemon juice'.format(lemon * servings_required / servings))
print('{:.2f} cup(s) water'.format(water * servings_required / servings))
print('{:.2f} cup(s) agave nectar'.format(nectar * servings_required / servings))

print('\nLemonade ingredients - yields {:.2f} servings'.format(servings_required))
print('{:.2f} gallon(s) lemon juice'.format(lemon * servings_required / servings / 16))
print('{:.2f} gallon(s) water'.format(water * servings_required / servings / 16))
print('{:.2f} gallon(s) agave nectar'.format(nectar * servings_required / servings / 16))

