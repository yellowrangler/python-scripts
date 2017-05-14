#!/usr/bin/env python

# crontab -l or -e setup
# 15 * * * * /home/tarryc/Development/python-scripts/checkWanIP.py

import urllib2
import smtplib

import pdb

# functions
def sendemailmsg(previouswanip,currentwanip):
    htmlserver = 'daisy'
    gmail_user = 'tcutler.business@gmail.com'  
    gmail_password = 'yellowrangler'

    sent_from = gmail_user 
    sent_to = 'tarrant.cutler@gmail.com, tzjamieson@yahoo.com'
    subject = 'IP address change for ' + htmlserver 
    body = "Yo Yo Yo!\n\nPrev wanip:\t" + previouswanip + "\nNew wanip:\t" + currentwanip

    msg = "\r\n".join([
      "From: "+sent_from,
      "To: "+sent_to,
      "Subject: "+subject,
      "",
      body
  ])
    try:
        # pdb.set_trace()

        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        # smtp_server.set_debuglevel(1)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, sent_to, msg)
        smtp_server.quit()
        print 'Email sent!'
    except:  
        print 'Something went wrong...'

# First we get the current WAN IP
response = urllib2.urlopen('http://www.myexternalip.com/raw')
currentwanip = response.read().strip()

#We get the previous WAN IP
f = open('/home/tarryc/Development/python-scripts/currentwanip.txt')
previouswanip = f.read().strip() 
f.close()

#Compare the previous WAN IP to current
if currentwanip != previouswanip:
    # send email to me if mismatch
    sendemailmsg(previouswanip,currentwanip)

    # write new wanip to file
    f = open('/home/tarryc/Development/python-scripts/currentwanip.txt','w')
    f.write(currentwanip) 
    f.close 
