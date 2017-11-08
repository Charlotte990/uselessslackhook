#!/usr/local/bin/python

import requests
import datetime
import time
import calendar

dayNow = datetime.datetime.today().weekday()
timeNow = datetime.datetime.now().time()
start = datetime.time(9,00)
end = datetime.time(16,00)

if dayNow < 5 :
    if timeNow >= start and timeNow <= end:
        print(timeNow.strftime('%H %M %S'), calendar.day_name[dayNow])
        r = requests.post("YOURWEBHOOKGOESHERE", data="{\"username\":	\"yabotname\", \"channel\": \"#pickyourchannel\", \"icon_emoji\": \":octopus:\", \"text\": \"Let's get drunk? :beer:\"}")
        print(r.status_code, r.reason)
	time.sleep(86400)
