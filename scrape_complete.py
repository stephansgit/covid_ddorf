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

""" # create reference file
refdat = str(cntnt)
reffile = open("corona_düsseldorf_news_all", "w")
reffile.write(refdat)
reffile.close() 
 """

# open reference file
crn_ddorf = open("corona_düsseldorf_news_all", "r")
crn_ddorf_dat = crn_ddorf.read()
crn_ddorf.close()


# read current homepage
print("Reading website...")
pth_tday = "https://corona.duesseldorf.de/news"
getPage = requests.get(pth_tday)
getPage.raise_for_status()
pg = bs4.BeautifulSoup(getPage.text, 'html.parser')
latest = pg.select('.text-red')
cntnt = re.findall('<h4 class="text-red">(.+?)</h4>', str(latest))
print("Website gives as latest entry > "+str(cntnt[0]))

# Check if page is updated
if str(cntnt) == crn_ddorf_dat:
    sys.exit("Content does not seem to have changed on ")
else:
    
    # create new reference file
    refdat = str(cntnt)
    reffile = open("corona_düsseldorf_news_all", "w")
    reffile.write(refdat)
    reffile.close() 

    msg = MIMEText(pth_tday)
    msg['From'] = "stephan.sprenger@web.de"
    msg['To'] = "stephan.sprenger@uniper.energy"
    msg['Subject'] = 'Corona Düsseldorf Webseite hat sich geändert!'
 
    conn = smtplib.SMTP('smtp.web.de', 587) # smtp address and port
    # conn.set_debuglevel(debuglevel = 2)
    conn.ehlo() # call this to start the connection
    conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
    conn.login('stephan.sprenger@web.de', 'ssp*90SSP')
    conn.send_message(msg, msg['From'], msg['To'])
    conn.quit()



