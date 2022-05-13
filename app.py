from datetime import date
from dateutil.relativedelta import relativedelta

# TODO: Age calculation
birthday = date(1987, 11, 15)
today = date.today()

age = relativedelta(today, birthday)
print(f"Current age is {age.years} years, {age.months} months, and {age.days} days.")