from datetime import date
from dateutil.relativedelta import relativedelta


# Get birthday from user
month = int(input("Birth month: "))
day = int(input("Birth day: "))
year = int(input("Birth year: "))
birthday = date(year, month, day)
today = date.today()

age = relativedelta(today, birthday)
print(f"Current age is {age.years} years, {age.months} months, and {age.days} days.")