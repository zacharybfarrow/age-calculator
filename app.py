from datetime import date
from dateutil.relativedelta import relativedelta


# Get birthday from user, handle exceptions

while True:
    try:
        month = abs(int(input("Birth month: ")))
        break
    except ValueError:
        print("Please enter numeric value.")

while True:
    try:
        day = abs(int(input("Birth day: ")))
        break
    except ValueError:
        print("Please enter numeric value.")

while True:
    try:
        year = abs(int(input("Birth year (YYYY): ")))
        break
    except ValueError:
        print("Please enter numeric value.")

birthday = date(year, month, day)
today = date.today()

age = relativedelta(today, birthday)
print(f"Current age is {age.years} years, {age.months} months, and {age.days} days.")