from bs4 import BeautifulSoup
import requests, re, os, sys
import urllib2

url = 'http://172.18.6.180/ID/Handouts.do'

req = requests.get(url)
resp = req.text

soup = BeautifulSoup(resp)

all_anchor = soup.findAll('a')

pattern = re.compile(r'/HANDOUTS/.*\.pdf')

d = 'Party'
if not os.path.exists(d):
    os.makedirs(d)

os.chdir('/Users/ankitsultana/Desktop/' + d)

for atags in all_anchor:
    tempurl = 'http://172.18.6.180'
    atagsString = str(atags)
    if re.search('/HANDOUTS/.*\.pdf', atagsString) != None:
        m = re.search(r'(?<=").*(?=")', atagsString)
        anotherM = re.search('(?<=HANDOUTS\/).*(?=")', atagsString)
        fileName = anotherM.group(0)
        tempurl += m.group(0)
        another_req = urllib2.urlopen(tempurl)
        data = another_req.read()
        File = open(fileName, 'wb')
        try:
            File.write(data)
        except Exception, e:
            print 'FAILED: ' + fileName
            print e
        File.close()
