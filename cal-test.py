# calendar.py

import calendar

# Map weekday numbers to names using the calendar module
daysofweek = {i: name for i, name in enumerate(calendar.day_name)}

# Set Sunday (6) as the first weekday and print its name
# calendar.setfirstweekday(6)

# print(daysofweek[calendar.firstweekday()])

yy = 2026
mm = 2
# print(calendar.month(yy,mm))


month = list(range(1,13))

for m in month:
    print(calendar.month(26,m))


