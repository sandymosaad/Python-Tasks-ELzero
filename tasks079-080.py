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

#---------------------task 1 done ---------------------
#------------------------------------------------------
'''
problem 02:
Write a Python program that prints today’s date and time in multiple formats.
You should display the current date in several different string representations as shown in the examples below.
Examples of date formats to display:
# Today Is "2021, 8, 10"
"2021-08-10"
"Aug 10, 2021"
"10 - Aug - 2021"
"10 / Aug / 21"
"10 / August / 2021"
"Tue, 10 August 2021"
'''
today =datetime.date.today()
print(f'Today: {today}')
today_2 = today.strftime('%b %d, %Y')
print(f'Today: {today_2}')
today_3 =today.strftime('%d-%b-%Y')
print(f'Today: {today_3}')
today_4 =today.strftime('%d / %b / %Y')
print(f'Today: {today_4}')
today_5 =today.strftime('%d / %B / %Y')
print(f'Today: {today_5}')
today_6 =today.strftime('%a, %d  %B  %Y')
print(f'Today: {today_6}')
#---------------------task 2 done ---------------------
#------------------------------------------------------