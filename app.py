from datetime import date

# TODO: Age calculation
birthday = date(1987, 11, 15)
today = date.today()

age_in_days = today - birthday
print(age_in_days)

# Not accurate - does not account for whether birthday has passed this year or not.
age_in_years = today.year - birthday.year
print(age_in_years)

# Count years, looking for leap years along the way