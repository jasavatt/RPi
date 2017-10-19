#!/usr/bin/python

from sensors import BMP280, HTU21D, light
import datetime
import csv
import urllib2

baseURL = 'https://api.thingspeak.com/update?api_key=H3SMS2GSCA1HGCDV'

s1 = BMP280.BMP280()
s2 = HTU21D.HTU21D()

#read sensors
h = s2.read_humidity()
t = s1.read_temperature()
p = s1.read_pressure()
l = light.getlight()

#t(temp) to F
f = (t*1.8+32)

#convert to string and round
H = str(round(h,2))
T = str(round(f,2))
P = str(p)
L = str(round(l,2))

#debug print
print("Humidity is %s %%") %H
print("Temp is %s C") %round(t,2)
print("Temp is %s F") %round((t*1.8+32),2)
print("Presssure is %s Pa") %P
print("Light leve is %s lux") %L


#write to csv
f = open('/home/pi/Scripts/room2/data.csv','a')
now = datetime.datetime.now()
timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
myData = [timestamp,h,t,p]
w = csv.writer(f, dialect='excel')
w.writerow(myData)
f.close

#write to thingspeak
f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s&field3=%s&field4=%s" % (H, T, P, L))
print (f.read())
f.close()
