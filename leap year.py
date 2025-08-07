year=int(input("Enter a year: "))
if (year % 400 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(" is a leap year", year)
else:
    print(" is not a leap year",year)