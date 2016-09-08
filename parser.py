
import codecs
import requests
import os
import time
import datetime

fileName = '1.txt'
    #'../2016-09-06PRock.dpm'
tags = ['Music-ROCK', 'RU', 'Spot']
tagsChange = {'Jingles-ROCK':'Реклама', 'Spot':'cn'}
url='http://radio.westele.com.ua/api/audio/save?data='
station = '37'
param = '&station='

fo = codecs.open(fileName, 'r', 'cp1251', buffering = 0)
#fo.seek(-1, 2)

line =''
i = 1
#print (fo.tell())

while 1:
    where = fo.tell()
    print('while')
    print(where)
   # print(where)
    line = fo.readline()
    print(line)
    if not line:
        time.sleep(1)
        print ('if')
        fo.seek(where)

        print(fo.seek(where))
    else:
        print (line) # already has newline
        #words = line.split('\t')
        #if words[3] in tags:
        #    print('Get')
        #    sendWord = (words[4].replace(' ', '+')).strip('.mp3')
        #if words[3] in tagsChange:
        #    print('Get')
        #    print(tagsChange.get(words[3]))

#while line.find('\n'):
#    line = fo.read()
#    i=i+1
#    fo.seek(-i, 1)
#fo.close()
#words = line.split('\t')

#print(words)
#sendWord = (words[4].replace(' ', '+')).strip('.mp3')
#print (sendWord)
#if words[3] in tags:
#    print ('Get')
#if words[3]in tagsChange:
#    print ('Get')
#    print (tagsChange.get(words[3]))


#r = requests.get('https://api.github.com/user', auth=('travers.nk@gmail.com', 'nataliia1'))
#print (r.status_code)
#tr = requests.get(url+sendWord+param+station)
#print (tr.status_code)

#http://radio.westele.com.ua/api/audio/save?data=Sia+-+Cheap+Thrills&station=36

#curTime = time.time()
#timeNow = datetime.datetime.today()
#mtime = os.path.getmtime(fileName)
#mTime= datetime.datetime.fromtimestamp(mtime)

#print (datetime.timedelta(timeNow, mTime))