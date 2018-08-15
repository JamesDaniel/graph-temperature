from time import sleep
from serial import Serial

import datetime as dt

ser = Serial('/dev/ttyACM0', 9600)
lastMinute = -1

while True:
    temperatureC = str(ser.readline()).strip()
    if float(temperatureC) < 15.0 or float(temperatureC) > 30.0:
        print "Invalid temp: " + temperatureC
        continue
    if dt.datetime.now().minute != lastMinute:
        lastMinute = dt.datetime.now().minute
        csvline = str(dt.datetime.now().hour) + ":" + str(dt.datetime.now().minute) + ":00" + "," + temperatureC + "\n"
        with open('sample.csv','a') as fd:
            fd.write(csvline)
	    print csvline.strip()
            sleep(5)

