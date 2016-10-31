import serial  #The library for communicating with the arduino

import os

import re
import string

#Connect to the arduino
ser = serial.Serial('/dev/tty.usbmodem1411', 9600)

while 1:
        data = ""

#get the data
#also below removes any non alphanumeric characters and newline to be able to read string
        data = ser.readline()
	pattern = re.compile('\W')
	string = re.sub(pattern, '', data)
        print string.rstrip("\n")
        if string == 'UpArrow':
		print 'Upp Arrow was pressed'
        if string == 'DownArrow':
		print 'Down Arrow was pressed'
        if string == 'LeftArrow':
		print 'Left Arrow was pressed'
        if string == 'RightArrow':
		print 'Right Arrow was pressed'
        if string == 'OK':
		print 'OK was pressed'
        if string == 'STAR':
		print 'STAR was pressed'
        if string == 'HASH':
		print 'HASH was pressed'
        if string == '0':
		print '0 was pressed'
        if string == '1':
		print '1 was pressed'
        if string == '2':
		print '2 was pressed'
	if string == '3':
		print '3 was pressed'
        if string == '4':
		print '4 was pressed'
        if string == '5':
		print '5 was pressed'
	if string == '6':
		print '6 was pressed'
        if string == '7':
		print '7 was pressed'
        if string == '8':
		print '8 was pressed'
	if string == '9':
		print '9 was pressed'




