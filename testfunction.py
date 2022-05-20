from datetime import date
from dateutil.relativedelta import relativedelta


# Get birthday from user, handle exceptions

while True:
    try:
        month = int(input("Birth month: "))
        break
    except ValueError:
        print("Please enter numeric value.")

while True:
    try:
        day = int(input("Birth day: "))
        break
    except ValueError:
        print("Please enter numeric value.")

while True:
    try:
        year = int(input("Birth year (YYYY): "))
        break
    except ValueError:
        print("Please enter numeric value.")

try:
    birthday = date(year, month, day)
except ValueError as e:
    print("Error: ", e)
else:
    today = date.today()
    age = relativedelta(today, birthday)

    print(f"Current age is {age.years} years, {age.months} months, and {age.days} days.")