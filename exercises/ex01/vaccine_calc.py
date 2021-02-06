"""A vaccination calculator."""

__author__ = "730318823"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

pop: int = int(input("Population: "))
admin: int = int(input("Doses already administered: "))
per_day: int = int(input("Doses per day: "))
target: float = float(input("Target percent vaccinated: "))

days_remaining: int = int(((pop * 2) * target / 100) / per_day)

today: datetime = datetime.today()
days_left: timedelta = timedelta(days_remaining)
end: datetime = today + days_left

target: int = round(target)

print_dates: str = end.strftime("%B %d, %Y")
print("We will reach " + str(target) + "% vaccination in " + str(days_remaining) + " days, which falls on " + print_dates + ".")

