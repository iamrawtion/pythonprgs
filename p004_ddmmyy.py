#!/usr/bin/python
flag=0
date=input("enter a date in DDMMYY format : ")
if int(date[:2])>0 and int(date[:2])<32 :
    print "date %d is valid"%int(date[:2])
else:
    print "date %d is invalid"%int(date[:2])
    flag=1
if int(date[2:4])>0 and int(date[2:4])<13:
    print "month %d is valid"%int(date[2:4])
else:
    print "month %d is invalid"%int(date[2:4])
    flag=1
if int(date[4:6])>=00 and int(date[4:6])<100:
    print "year %d is valid"%int(date[4:6])
else:
    print "year %d is invalid"%int(date[4:6])
    flag=1

if flag==1:
    print "invalid"
else:
    print "valid"


