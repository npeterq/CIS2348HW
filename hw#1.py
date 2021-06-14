"Peter Nguyen"
"6/14/2021"
"CIS2348"
"1860823"

from datetime import date


print("Birthday Calculator")
print("Current Day")
month = int(input("Month: "))
day = int(input("Day: "))
year = int(input("Year: "))

print("Birthday")
bmonth = int(input("Month: "))
bday = int(input("Day: "))
byear = int(input("Year: "))
print("You are", year - byear - ((month, day) < (bmonth, bday)), "years old.")
if day == bday and month == bmonth:
    print("Happy Birthday!")
