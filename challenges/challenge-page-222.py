from datetime import datetime
import pytz

portland = datetime.now(pytz.timezone('US/Pacific')).time()
newYork = datetime.now(pytz.timezone('America/New_York')).time()
london = datetime.now(pytz.timezone('Europe/London')).time()

por = int(portland.strftime('%H'))
new = int(newYork.strftime('%H'))
lon = int(london.strftime('%H'))

porStr = portland.strftime('%I:%M %p')
newStr = newYork.strftime('%I:%M %p')
lonStr = london.strftime('%I:%M %p')

if 9 < por < 17:
    print("It is {} in Portland, OR. \
          \nWe are currently open at this location.\
          \nOur operating hours are from 9:00 AM to 5:00 PM\n".format(porStr))
else:
    print("It is {} in Portland, OR. \
          \nWe are currently closed at this location.\
          \nOur operating hours are from 9:00 AM to 5:00 PM\n".format(porStr))

if 9 < new < 17:
    print("It is {} in New York, NY. \
          \nWe are currently open at this location.\
          \nOur operating hours are from 9:00 AM to 5:00 PM\n".format(newStr))
else:
    print("It is {} in New York, NY. \
          \nWe are currently closed at this location.\
          \nOur operating hours are from 9:00 AM to 5:00 PM\n".format(newStr))

if 9 < lon < 17:
    print("It is {} in London, England. \
          \nWe are currently open at this location.\
          \nOur operating hours are from 9:00 AM to 5:00 PM\n".format(lonStr))
else:
    print("It is {} in London, England. \
          \nWe are currently closed at this location.\
          \nOur operating hours are from 9:00 AM to 5:00 PM\n".format(lonStr))
