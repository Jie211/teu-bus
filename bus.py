import urllib2
from bs4 import BeautifulSoup
import  csv

html = urllib2.urlopen("http://www.teu.ac.jp/campus/access/2015_kihon-a_bus.html")
soup = BeautifulSoup(html,'html.parser')
table = soup.find_all('table')
f1=open('bus1.csv','w')
writer1=csv.writer(f1, lineterminator='\n')
f2=open('bus2.csv','w')
writer2=csv.writer(f2, lineterminator='\n')
f3=open('bus3.csv','w')
writer3=csv.writer(f3, lineterminator='\n')
t1 = table[0].find_all('tr')
t2 = table[1].find_all('tr')
t3 = table[2].find_all('tr')
data1 = []

data2 = []

data3 = []

for row in t1:
    cols = row.find_all('td')
    d = []
    for i in xrange(3):
        if len(cols)>0:
            d.append(cols[i].text.strip())
    if len(cols)>0:
        data1.append(d)

for row in t2:
    cols = row.find_all('td')
    d = []
    for i in xrange(3):
        if len(cols)>0:
            d.append(cols[i].text.strip())
    if len(cols)>0:
        data2.append(d)

for row in t3:
    cols = row.find_all('td')
    d = []
    for i in xrange(3):
        if len(cols)>0:
            d.append(cols[i].text.strip())
    if len(cols)>0:
        data3.append(d)

st=['shuttle','shuttle','shuttle']

for i in data1:
    try:
        writer1.writerow(i)
    except Exception, e:
        t = str(type(e))
        if t == '<type \'exceptions.UnicodeEncodeError\'>' :
            writer1.writerow(st)
            continue
        else:
            print e
            print type(e)

for i in data2:
    try:
        writer2.writerow(i)
    except Exception, e:
        t = str(type(e))
        if t == '<type \'exceptions.UnicodeEncodeError\'>' :
            writer2.writerow(st)
            continue
        else:
            print e
            print type(e)

for i in data3:
    try:
        writer3.writerow(i)
    except Exception, e:
        t = str(type(e))
        if t == '<type \'exceptions.UnicodeEncodeError\'>' :
            writer3.writerow(st)
            continue
        else:
            print e
            print type(e)
f1.close()
f2.close()
f3.close()