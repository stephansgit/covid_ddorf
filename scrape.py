#!/usr/bin/env python3

import bs4
import requests
import datetime
from babel.dates import format_date, format_datetime, format_time
import funcs
import re
import smtplib
from email.mime.text import MIMEText
import os
import sys


pth_tday = funcs.create_path(asof = funcs.create_date(), pth = "https://corona.duesseldorf.de/news/die-aktuellen-coronazahlen-vom-")
print("The current path is "+pth_tday[0])

if os.path.isfile(pth_tday[1]):
    sys.exit("File is already there; quitting.")

print("Reading website...")
getPage = requests.get(pth_tday[0])
getPage.raise_for_status()
pg = bs4.BeautifulSoup(getPage.text, 'html.parser')
latest = pg.select('.lead')
cntnt = re.findall('<p>(.+?)</p>', str(latest))

print("Website gives "+str(cntnt))

print("Preparing E-Mail")
msg = MIMEText(''.join(cntnt))
msg['From'] = "stephan.sprenger@web.de"
msg['To'] = "stephan.sprenger@uniper.energy"
msg['Subject'] = 'Düsseldorf Corona Zahlen '+pth_tday[1]

print("Connecting to server...") 
conn = smtplib.SMTP('smtp.web.de', 587) # smtp address and port
# conn.set_debuglevel(debuglevel = 2)
conn.ehlo() # call this to start the connection
conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
conn.login('stephan.sprenger@web.de', 'ssp*90SSP')
conn.send_message(msg, msg['From'], msg['To'])
conn.quit()
print("Closing Server connection")

checkfile = pth_tday[1]
open(checkfile, "w").close()
print("Checkfile written")
