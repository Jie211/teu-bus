# -*- coding: utf-8 -*-
import csv
import datetime
import sys
import urllib2

book1=[]
book2=[]
book3=[]

output1=False
output2=False
output3=False

d1=urllib2.urlopen("https://raw.githubusercontent.com/Jie211/teu-bus/master/bus1.csv")
d2=urllib2.urlopen("https://raw.githubusercontent.com/Jie211/teu-bus/master/bus2.csv")
d3=urllib2.urlopen("https://raw.githubusercontent.com/Jie211/teu-bus/master/bus1.csv")

for line in d1:
    book1.append(line.strip().split(","))

for line in d2:
    book2.append(line.strip().split(","))

for line in d3:
    book3.append(line.strip().split(","))

message='-----'

nowtime=datetime.datetime.now()
# nowtime=datetime.datetime(2016,4,29,8,11,11,11)

lenbook1=len(book1)
lenbook2=len(book2)
lenbook3=len(book3)

for i in xrange(lenbook1):
    tar=book1[i][0]

    if tar.find(':') == -1:
        continue

    tar2=[tar[0:tar.find(':')],tar[tar.find(':')+1:]]

    tartime=datetime.datetime(nowtime.year, nowtime.month, nowtime.day, hour=int(tar2[0]), minute=int(tar2[1]),second=00,microsecond=00)

    if tartime >= nowtime:
        if book1[i-1][0] == 'shuttle':
            message += "\n八王子行き今はシャットル運行中"
            output1=True
            break
        message += "\n次の八王子行きのバスは"+tartime.strftime("%H:%M")+"から出発します．"
        output1=True
        break
    elif tartime == nowtime:
        pass
    else:
        pass
if output1==False:
    message += "\nもう八王子に行くバスがないですよ"



for i in xrange(lenbook2):
    tar=book2[i][0]

    if tar.find(':') == -1:
        continue

    tar2=[tar[0:tar.find(':')],tar[tar.find(':')+1:]]

    tartime=datetime.datetime(nowtime.year, nowtime.month, nowtime.day, hour=int(tar2[0]), minute=int(tar2[1]),second=00,microsecond=00)

    if tartime >= nowtime:
        if book2[i-1][0] == 'shuttle':
            message += "\nみなみ野行き今はシャットル運行中"
            output2=True
            break
        message += "\n次のみなみ野行きのバスは"+tartime.strftime("%H:%M")+"から出発します．"
        output2=True
        break
    elif tartime == nowtime:
        pass
    else:
        pass
if output2==False:
    message += "\nもうみなみ野に行くバスがないですよ"


for i in xrange(lenbook3):
    tar=book3[i][0]

    if tar.find(':') == -1:
        continue

    tar2=[tar[0:tar.find(':')],tar[tar.find(':')+1:]]

    tartime=datetime.datetime(nowtime.year, nowtime.month, nowtime.day, hour=int(tar2[0]), minute=int(tar2[1]),second=00,microsecond=00)

    if tartime >= nowtime:
        message += "\n次の学生会館行きのバスは"+tartime.strftime("%H:%M")
        output3=True
        break
    elif tartime == nowtime:
        pass
    else:
        pass
if output3==False:
    message += "\nもう学生会館に行くバスがないですよ"

print message
