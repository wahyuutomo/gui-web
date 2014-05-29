#!/usr/bin/env python

import webiopi
import datetime
import MySQLdb


GPIO = webiopi.GPIO

LIGHT = 17 # GPIO pin using BCM numbering

HOUR_ON  = 8  # Turn Light ON at 08:00
HOUR_OFF = 18 # Turn Light OFF at 18:00

auto = [0,0,0,0,0,0,0,0]
jamon = [0,0,0,0,0,0,0,0]
jamoff = [0,0,0,0,0,0,0,0]
meniton = [0,0,0,0,0,0,0,0]
menitoff = [0,0,0,0,0,0,0,0]


# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    # initialitation Button Home Away
    GPIO.setFunction(7, GPIO.OUT)
    GPIO.setFunction(8, GPIO.OUT)
    GPIO.setFunction(25, GPIO.OUT)
    GPIO.setFunction(11, GPIO.OUT)
    mcp = webiopi.deviceInstance("mcp") # retrieve the device named "mcp" in the configuration 
    mcp2 = webiopi.deviceInstance("mcp2")
    mcp3 = webiopi.deviceInstance("mcp3")

    # Setup mcp
    for x in range(0, 8):
      mcp.setFunction(x, GPIO.OUT)

    # Setup mcp2
    for x in range(0, 8):
      mcp2.setFunction(x, GPIO.OUT)

    # Setup mcp3
    for x in range(0, 8):
      mcp3.setFunction(x, GPIO.OUT)

    # Setup mcp LOW
    for x in range(0, 8):
      mcp.digitalWrite(x, GPIO.LOW)

    # Setup mcp2
    for x in range(0, 8):
      mcp2.digitalWrite(x, GPIO.LOW)

    # Setup mcp3
    for x in range(0, 8):
      mcp3.digitalWrite(x, GPIO.LOW)

    # retrieve current datetime
    now = datetime.datetime.now()
	# test if we are between ON time and tun the light ON
	initauto(auto,jamon,jamoff,meniton,menitoff)
    
   

# loop function is repeatedly called by WebIOPi 
def loop():
    # retrieve current datetime
    now = datetime.datetime.now()
	if (now.second==0):
		match(auto,jamon,jamoff,meniton,menitoff)
    
             
    if int (GPIO.digitalRead(7)) == 1 and int (GPIO.digitalRead(11)) == 0 :
      for x in range(0, 8):
         mcp.digitalWrite(x, GPIO.HIGH)
         mcp2.digitalWrite(x, GPIO.HIGH)
         mcp3.digitalWrite(x, GPIO.HIGH)
      GPIO.digitalWrite(7, GPIO.LOW)
      
    elif int (GPIO.digitalRead(11)) == 1 and int (GPIO.digitalRead(7)) == 0:
      for x in range(0, 7):
         mcp.digitalWrite(x, GPIO.LOW)
      for x in range(0, 8):
         mcp2.digitalWrite(x, GPIO.LOW)
         mcp3.digitalWrite(x, GPIO.HIGH)
      GPIO.digitalWrite(11, GPIO.LOW)

    if int (GPIO.digitalRead(8)) == 1 :
      for x in range(0, 8):
         mcp.digitalWrite(x, GPIO.HIGH)
         mcp2.digitalWrite(x, GPIO.HIGH)
         mcp3.digitalWrite(x, GPIO.HIGH)
      webiopi.sleep(0.2)
      for x in range(0, 8):
         mcp.digitalWrite(x, GPIO.LOW)
         mcp2.digitalWrite(x, GPIO.LOW)
         mcp3.digitalWrite(x, GPIO.LOW)
      
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    # destroy button Home Away
    GPIO.digitalWrite(7, GPIO.LOW)
    GPIO.digitalWrite(8, GPIO.LOW)
    GPIO.digitalWrite(25, GPIO.LOW)
    GPIO.digitalWrite(11, GPIO.LOW)
    GPIO.setFunction(7, GPIO.IN)
    GPIO.setFunction(8, GPIO.IN)
    GPIO.setFunction(25, GPIO.IN)
    GPIO.setFunction(11, GPIO.IN)

    mcp  = webiopi.deviceInstance("mcp")       # retrieve the device named "mcp" in the configuration 
    mcp2 = webiopi.deviceInstance("mcp2")
    mcp3 = webiopi.deviceInstance("mcp3")
    
    
    # Setup mcp LOW
    for x in range(0, 8):
      mcp.digitalWrite(x, GPIO.LOW)

    # Setup mcp2
    for x in range(0, 8):
      mcp2.digitalWrite(x, GPIO.LOW)

    # Setup mcp3
    for x in range(0, 8):
      mcp3.digitalWrite(x, GPIO.LOW)
	
    for x in range(0, 8):
      mcp.setFunction(x, GPIO.IN)

    # Setup mcp2
    for x in range(0, 8):
      mcp2.setFunction(x, GPIO.IN)

    # Setup mcp3
    for x in range(0, 8):
      mcp3.setFunction(x, GPIO.IN)



@webiopi.macro
def getLightHours():
    return "%d;%d" % (HOUR_ON, HOUR_OFF)

@webiopi.macro
def setLightHours(on, off):
    global HOUR_ON, HOUR_OFF
    HOUR_ON = int(on)
    HOUR_OFF = int(off)
    return getLightHours()

@webiopi.macro
def update():
	global auto = [0,0,0,0,0,0,0,0]
	global jamon = [0,0,0,0,0,0,0,0]
	global jamoff = [0,0,0,0,0,0,0,0]
	global meniton = [0,0,0,0,0,0,0,0]
	global menitoff = [0,0,0,0,0,0,0,0]

	db = MySQLdb.connect("localhost","root","1214174","monitoring")
	cursor = db.cursor()
	cursor.execute("SELECT * FROM lampu")
	data=cursor.fetchall()
	
	i = 0
	for col in data:
		auto[i] = col[2]
		jamon[i] = col[3]
		meniton[i] = col[4]
		jamoff[i] = col[5]
		menitoff[i] = col[6]	
		i = i+1
	db.close()
	
	return

def match(auto,jamon,jamoff,meniton,menitoff):
	now = datetime.datime.now()
	
	#LAMPU 0
	if (auto[0]==1):
		if ((now.hour == jamon[0]) and (now.minute == meniton[0])):
			print "Lampu 0 nyala"
			if (mcp.digitalRead(0) == GPIO.LOW):
				mcp.digitalWrite(0, GPIO.HIGH)
				
		if ((now.hour == jamoff[0]) and (now.minute == menitoff[0])):
			print "Lampu 0 mati"
			if (mcp.digitalRead(0) == GPIO.HIGH):
				mcp.digitalWrite(0, GPIO.LOW)	
            
	#LAMPU 1
	if (auto[1]==1):
		if ((now.hour == jamon[1]) and (now.minute == meniton[1])):
			print "Lampu 1 nyala"
			if (mcp.digitalRead(1) == GPIO.LOW):
				mcp.digitalWrite(1, GPIO.HIGH)
				
		if ((now.hour == jamoff[1]) and (now.minute == menitoff[1])):
			print "Lampu 1 mati"
			if (mcp.digitalRead(1) == GPIO.HIGH):
				mcp.digitalWrite(1, GPIO.LOW)	
	
	#LAMPU 2
	if (auto[2]==1):
		if ((now.hour == jamon[2]) and (now.minute == meniton[2])):
			print "Lampu 2 nyala"
			if (mcp.digitalRead(2) == GPIO.LOW):
				mcp.digitalWrite(2, GPIO.HIGH)
				
		if ((now.hour == jamoff[2]) and (now.minute == menitoff[2])):
			print "Lampu 2 mati"
			if (mcp.digitalRead(2) == GPIO.HIGH):
				mcp.digitalWrite(2, GPIO.LOW)	
	
	#LAMPU 3
	if (auto[3]==1):
		if ((now.hour == jamon[3]) and (now.minute == meniton[3])):
			print "Lampu 3 nyala"
			if (mcp.digitalRead(3) == GPIO.LOW):
				mcp.digitalWrite(3, GPIO.HIGH)
				
		if ((now.hour == jamoff[3]) and (now.minute == menitoff[3])):
			print "Lampu 3 mati"
			if (mcp.digitalRead(3) == GPIO.HIGH):
				mcp.digitalWrite(3, GPIO.LOW)	

	#LAMPU 4
	if (auto[4]==1):
		if ((now.hour == jamon[4]) and (now.minute == meniton[4])):
			print "Lampu 4 nyala"
			if (mcp2.digitalRead(0) == GPIO.LOW):
				mcp2.digitalWrite(0, GPIO.HIGH)
				
		if ((now.hour == jamoff[4]) and (now.minute == menitoff[4])):
			print "Lampu 4 mati"
			if (mcp2.digitalRead(0) == GPIO.HIGH):
				mcp2.digitalWrite(0, GPIO.LOW)	

	#LAMPU 5
	if (auto[5]==1):
		if ((now.hour == jamon[5]) and (now.minute == meniton[5])):
			print "Lampu 5 nyala"
			if (mcp2.digitalRead(1) == GPIO.LOW):
				mcp2.digitalWrite(1, GPIO.HIGH)
				
		if ((now.hour == jamoff[5]) and (now.minute == menitoff[5])):
			print "Lampu 5 mati"
			if (mcp2.digitalRead(1) == GPIO.HIGH):
				mcp2.digitalWrite(1, GPIO.LOW)	

	#LAMPU 6
	if (auto[6]==1):
		if ((now.hour == jamon[6]) and (now.minute == meniton[6])):
			print "Lampu 6 nyala"
			if (mcp2.digitalRead(2) == GPIO.LOW):
				mcp2.digitalWrite(2, GPIO.HIGH)
				
		if ((now.hour == jamoff[6]) and (now.minute == menitoff[6])):
			print "Lampu 6 mati"
			if (mcp2.digitalRead(2) == GPIO.HIGH):
				mcp2.digitalWrite(2, GPIO.LOW)	

	#LAMPU 7
	if (auto[7]==1):
		if ((now.hour == jamon[7]) and (now.minute == meniton[7])):
			print "Lampu 7 nyala"
			if (mcp2.digitalRead(3) == GPIO.LOW):
				mcp2.digitalWrite(3, GPIO.HIGH)
				
		if ((now.hour == jamoff[7]) and (now.minute == menitoff[7])):
			print "Lampu 7 mati"
			if (mcp2.digitalRead(3) == GPIO.HIGH):
				mcp2.digitalWrite(3, GPIO.LOW)	

	return

def initauto(auto,jamon,jamoff,meniton,menitoff):
	now = datetime.datetime.now()
	i = 0
	while (i<4):
		if (auto[i]==1):
			if (jamon[i]<jamoff[i]):
				if ((now.hour>=jamon[i]) and (now.hour<=jamoff[i])):
					if (now.hour==jamon[i]):
						if (now.minute>=meniton[i]):
							mcp.digitalWrite(i, GPIO.HIGH)
#						else :
#							print "lampu %d mati" %i
					elif (now.hour==jamoff[i]):
						if (now.minute<menitoff[i]):
							mcp.digitalWrite(i, GPIO.HIGH)
#						else :
#							print "lampu %d mati" %i
					else:
						mcp.digitalWrite(i, GPIO.HIGH)
#				else:
#					print "lampu %d mati" %i				
					
			elif (jamon[i]>jamoff[i]):
				if ((now.hour>=jamon[i]) or (now.hour<=jamoff[i])):
					if (now.hour==jamon[i]):
						if (now.minute>=meniton[i]):
							mcp.digitalWrite(i, GPIO.HIGH)
#						else :
#							print "lampu %d mati" %i
					elif (now.hour==jamoff[i]):
						if (now.minute<menitoff[i]):
							mcp.digitalWrite(i, GPIO.HIGH)
#						else :
#							print "lampu %d mati" %i
					else:
						mcp.digitalWrite(i, GPIO.HIGH)					
#				else:
#					print "lampu %d mati" %i
					
			elif (jamon[i]==jamoff[i]):
				if (meniton[i]<menitoff[i]):
					if ((now.minute>=meniton[i]) and (now.minute <= menitoff[i])):
						mcp.digitalWrite(i, GPIO.HIGH)
#					else:
#						print "lampu %d mati" %i
				elif (meniton[i]>menitoff[i]):
					if ((now.minute>=meniton[i]) or (now.minute<=menitoff[i])):
						mcp.digitalWrite(i, GPIO.HIGH)
#					else:
#						print "lampu %d mati" %i
				elif (meniton[i] == menitoff[i]):
						mcp.digitalWrite(i, GPIO.HIGH)
#				else:
#					print "lampu %d mati" %i
#		else:
#			print "lampu %d mati" %i

		if (auto[i+4]==1):
			#print jamon[i+4],jamoff[i+4]
			if (jamon[i+4]<jamoff[i+4]):
				if ((now.hour>=jamon[i+4]) and (now.hour<=jamoff[i+4])):
					if (now.hour==jamon[i+4]):
						if (now.minute>=meniton[i+4]):
							mcp2.digitalWrite(i, GPIO.HIGH)
#						else :
#							print "lampu %d mati" %(i+4)
					elif (now.hour==jamoff[i+4]):
						if (now.minute<menitoff[i+4]):
							mcp2.digitalWrite(i, GPIO.HIGH)
#						else :
#							print "lampu %d mati" %(i+4)
					else:
						mcp2.digitalWrite(i, GPIO.HIGH)
#				else:
#					print "lampu %d mati" %(i+4)
					
			elif (jamon[i+4]>jamoff[i+4]):
				if ((now.hour>=jamon[i+4]) or (now.hour<=jamoff[i+4])):
					if (now.hour==jamon[i+4]):
						if (now.minute>=meniton[i+4]):
							mcp2.digitalWrite(i, GPIO.HIGH)
#						else :
#							print "lampu %d mati" %(i+4)
					elif (now.hour==jamoff[i+4]):
						if (now.minute<menitoff[i+4]):
							mcp2.digitalWrite(i, GPIO.HIGH)
#						else :
#							print "lampu %d mati" %(i+4)
					else:
						mcp2.digitalWrite(i, GPIO.HIGH)
#				else:
#					print "lampu %d mati" %(i+4)
			elif (jamon[i+4]==jamoff[i+4]):
				if (meniton[i+4]<menitoff[i+4]):
					if ((now.minute>=meniton[i+4]) and (now.minute<=menitoff[i+4])):
						mcp2.digitalWrite(i, GPIO.HIGH)
#					else:
#						print "lampu %d mati" %(i+4)
				elif (meniton[i+4]>menitoff[i+4]):
					if ((now.minute>=meniton[i+4]) or (now.minute<=menitoff[i+4])):
						mcp2.digitalWrite(i, GPIO.HIGH)
#					else:
#						print "lampu %d mati" %(i+4)
				elif (meniton[i+4] == menitoff[i+4]):
						mcp2.digitalWrite(i, GPIO.HIGH)
#				else:
#					print "lampu %d mati" %(i+4)
#		else:
#			print "lampu %d mati" %(i+4)
		i=i+1

	return
