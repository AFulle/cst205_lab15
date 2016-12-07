#CST 205 Lab 15: Python Standard Library
#Yulian
#Lyndsay
#Ahdia

#problem 1: Craps


#problem 2: Creates and prints calendar of user's birthday
def birthCalendar():
  import calendar
  y = int(requestString("Enter the year you were born:"))
  m = int(requestString("Enter the month(in number form) you were born:"))
  print(calendar.month(y, m))

#problem 2: Subtracts users birthday from current date and prints how many days until their birthday
def birthdays():
  from datetime import date
  today = date.today()
  y = today.year
  m = int(requestString("Enter the month(in number form) you were born:"))
  d = int(requestString("Enter the day(in number form) you were born:"))
  birthday = date(y, m, d)
  diff = birthday - today
  print ("%i day(s) until your birthday") % diff.days

#problem 2: Prints the day the Declaration of Independence was ratified
def decDate():
  from datetime import date
  day = date(1776, 7, 4).weekday()
  if day == 0:
    print "The Declaration of Independence was ratified on Monday"
  if day == 1:
    print "The Declaration of Independence was ratified on Tuesday"
  if day == 2:
    print "The Declaration of Independence was ratified on Wednesday"
  if day == 3:
    print "The Declaration of Independence was ratified on Thursday"
  if day == 4:
    print "The Declaration of Independence was ratified on Friday"
  if day == 5:
    print "The Declaration of Independence was ratified on Saturday"
  if day == 6:
    print "The Declaration of Independence was ratified on Sunday"
