# calendar.py

import calendar

import calendar

cal = calendar.Calendar(firstweekday=6)  # 0=Monday



# Map weekday numbers to names using the calendar module
daysofweek = {i: name for i, name in enumerate(calendar.day_name)}

# Set Sunday (6) as the first weekday and print its name
# calendar.setfirstweekday(6)

# print(daysofweek[calendar.firstweekday()])

yy = 2026
mm = 2
# print(calendar.month(yy,mm))


month = list(range(1,13))

#for m in month:
 #   print(calendar.month(26,m))



# print(cal.monthdatescalendar(2026, 2))
# print(cal.monthdayscalendar(2026,2))


# ASSIGNMENT
# print the month and year for the next friday the 13th.
# you'll need the current date and iterate over all the months
# and day is 13 and weekday friday then print month and year.

import datetime
''' This was the original code from AI.
today = datetime.date.today() # Gets today's date as a date object
year = today.year # Starts the search from the current year 
month = today.month # and month
'''

# Try to skip ahead to future, print later friday the 13ths (e.g. nov 26, aug 27)
today = datetime.date.today()
year = 2026
month = 5 # or set to 12, get august 2027 output.



while True:
	# Check day 13 of this month
	d = datetime.date(year, month, 13) # Creates a placeholder for the date, fixing date at 13 but month and year are variables
	if d >= today and d.weekday() == 4:  # 4 = Friday. Date is later than or equal to today's date, and weekday is always friday.
		print(f"Next Friday the 13th is: {d.strftime('%B %Y')}") 
        # This is a fancy thing that converts the date object to a string, 
        # in the format of Month (full name) and Year.
		break
	# Move to next month
	month += 1
	if month > 12:
		month = 1
		year += 1