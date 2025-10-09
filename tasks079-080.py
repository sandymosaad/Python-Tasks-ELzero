'''
problem 01:
Write a Python program that calculates the number of days between a given date and today’s date.

The given date is "2025-10-5".

You need to:

Convert the string date into a datetime.date object.

Get today’s date using datetime.date.today().

Subtract the two dates to find the difference in days.

Print the number of days between the two dates and today’s date itself.

'''
import datetime
target_date = datetime.datetime.strptime("2025-1-05", "%Y-%m-%d").date()
today = datetime.date.today()
difference = today - target_date

print(f"Today: {today}")
print(f'Target Date: {target_date}')
print(f"Difference: {difference.days} days")
