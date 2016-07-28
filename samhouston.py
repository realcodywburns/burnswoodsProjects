#!/usr/bin/python

import time
import urllib2
import json
import time


def webcall(startdate):
        url = "http://mypowerusage.samhouston.net/download_csv.php?accountId="+ accountID + "&startDate=" + startdate + "&endDate="+endDate+"&serviceType=Electric&recordInterval=Hourly&siteName=DEMO&pageName=UsageResidential"
        req = urllib2.Request(url)
        page = urllib2.urlopen(req).read()
        return page

#globals
#consider hiding account number from main code....
accountID = "85531"
start = ""
check = "Query was empty"
header = "Read Date,kWh,kwhRec,Cost,Meter Number,Avg F,Max F,Min F,"
endDate = "2020-02-08"
x=1


while x <> 0:

    #loop vars
    page = check
    x = 1
    loopTime = time.time()
    # reads the csv and finds the bottom date
    #f = open('/media/GLSHDD1/GLS/burnswoods/electric.csv', 'r')
    f = open('//Serverzero/gls hdd 1/burnswoods/electric.csv', 'r')
    line = f.readlines()

    while start == "":

        if check in line[len(line)-x]:
            x +=1
            #works back to find the last good line
            lastline = line[len(line)-x]
        elif start in line[len(line)-x]:
            x +=1
            lastline = line[len(line)-x]
        else:
            lastline = line[len(line)-x]

        array = lastline.split(",") # breaks up columns by comma
        date_is = array[0] # picks col 0
       #trim the hour off
        datesplit = date_is.split(" ")
        start = datesplit[0]

    f.close()
    #f = open('/media/GLSHDD1/GLS/burnswoods/electric.csv', 'a')
    f = open('//Serverzero/gls hdd 1/burnswoods/electric.csv', 'a')
    while check in page:
        page = webcall(start)

        if check in page:
            time.sleep(10)

    #remove the header
    page = page[58:]
    #print page
    #write the file
    f.write(page)
    f.close()

    #sleep for 12 hours
    #time.sleep(4320)
    #making a cron event so no need to sleep and waste resources
    x = 0
f.close()
exit
