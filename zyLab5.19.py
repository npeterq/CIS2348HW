"Peter Nguyen"
"6/14/2021"
"CIS2348"
"1860823"
"5.19 LAB: Leap year"

is_leap_year = False

input_year = int(input())

if (input_year % 400 == 0):
    is_leap_year = True
elif input_year % 100 == 0:
    is_leap_year = False
elif input_year % 4 == 0:
    is_leap_year = True

if (is_leap_year):
    print(input_year, "- leap year")
else:
    print(input_year, "- not a leap year")

