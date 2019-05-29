"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# Don't have time to keep hacking away at this, but at least I tried. ^_^

dt = datetime.now()
tc = calendar.TextCalendar()

if len(sys.argv) == 1:
  # no arguments; render calendar for current month and year
  tc.prmonth(dt.year, dt.month)
elif len(sys.argv) == 2:
  # one argument; render calendar for specific month in current year
  tc.prmonth(dt.year, int(sys.argv[1]))
elif len(sys.argv) == 3:
  # two arguments; render calendar for specific month and year
  tc.prmonth(int(sys.argv[2]), int(sys.argv[1]))
else:
  # error check!
  print('stahp! too much arg')
