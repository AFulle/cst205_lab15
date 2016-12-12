#CST 205 Lab 15: Python Standard Library
#Yulian
#Lyndsay
#Ahdia

#problem 1: Craps
from random import randint

def roll_dice(times=1):
  rolls = []
  for i in range(0, times):
    rolls = rolls + [randint(1,6)]
  
  printNow("Rolled "+str(times)+" dice. Result: " + ", ".join([str(x) for x in rolls]))
  return rolls

def play_craps():
  roll_two_dice = roll_dice(2)
  sum_dice = sum(roll_two_dice)
  printNow("Sum of dice: "+str(sum_dice))

  if sum_dice in [7, 11]:
    printNow("Instant win! :) Congratulations!")
    return
  elif sum_dice in [2, 3, 12]:
    printNow("Instant Lose. :( Hope you come back and play again.")
    return
  else:
    printNow("Got a point, your point is "+str(sum_dice)+".\n")
    point = sum_dice

  while true:
    new_sum = sum(roll_dice(2))
    printNow("Sum of dice: "+str(new_sum))
    if new_sum == point:
      printNow("You matched your point, you win! :) Congratulations!\n")
      break
    elif new_sum == 7:
      printNow("Bummer, you rolled a 7, you lose. :( Hope you come back and play again.\n")
      break
    else:
      printNow("No 7 and no Point, re-rolling.\n")

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

play_craps()