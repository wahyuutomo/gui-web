import webiopi
import datetime
import MySQLdb

GPIO = webiopi.GPIO # Helper for LOW/HIGH values

HEATER = 7 # Heater plugged on the Expander Pin 7
TEMP = 26
MIN = 23 # Minimum temperature in celsius
MAX = 26 # Maximum temperature in celsius
AUTO = True

auto = [0,0,0,0,0,0,0,0]
jamon = [0,0,0,0,0,0,0,0]
jamoff = [0,0,0,0,0,0,0,0]
meniton = [0,0,0,0,0,0,0,0]
menitoff = [0,0,0,0,0,0,0,0]


# setup function is automatically called at WebIOPi startup
def setup():
    # initialitation Button Home Away
    GPIO.setFunction(7, GPIO.OUT)
    GPIO.setFunction(8, GPIO.OUT)
    GPIO.setFunction(11, GPIO.OUT)
    GPIO.setFunction(17, GPIO.OUT)
    GPIO.setFunction(18, GPIO.OUT)
    GPIO.setFunction(25, GPIO.OUT)
    GPIO.setFunction(27, GPIO.OUT)
    mcp = webiopi.deviceInstance("mcp") # retrieve the device named "mcp" in the configuration 
    mcp2 = webiopi.deviceInstance("mcp2")
    mcp3 = webiopi.deviceInstance("mcp3")

    #setting PWM
    GPIO.setFunction(9, GPIO.PWM)
    GPIO.pwmWrite(9, 0)
    GPIO.setFunction(10, GPIO.PWM)
    GPIO.pwmWrite(10, 0)	

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
    initauto(auto,jamon,jamoff,meniton,menitoff,mcp,mcp2)


# loop function is repeatedly called by WebIOPi 
def loop():
    if (AUTO):
        tmp  = webiopi.deviceInstance("tmp")   # retrieve the device named "tmp" in the configuration
        mcp  = webiopi.deviceInstance("mcp")   # retrieve the device named "mcp" in the configuration 
        mcp2 = webiopi.deviceInstance("mcp2")
        mcp3 = webiopi.deviceInstance("mcp3")
		
        celsius = tmp.getCelsius() # retrieve current temperature
        print("Temperature: %f" % celsius)
        print "auto = %d,%d,%d,%d,%d,%d,%d,%d"%(auto[0],auto[1],auto[2],auto[3],auto[4],auto[5],auto[6],auto[7])
	print "jam on = %d,%d,%d,%d,%d,%d,%d,%d"%(jamon[0],jamon[1],jamon[2],jamon[3],jamon[4],jamon[5],jamon[6],jamon[7])
	print "jam off = %d,%d,%d,%d,%d,%d,%d,%d"%(jamoff[0],jamoff[1],jamoff[2],jamoff[3],jamoff[4],jamoff[5],jamoff[6],jamoff[7])
	print "menit on = %d,%d,%d,%d,%d,%d,%d,%d"%(meniton[0],meniton[1],meniton[2],meniton[3],meniton[4],meniton[5],meniton[6],meniton[7])
	print "menit off = %d,%d,%d,%d,%d,%d,%d,%d"%(menitoff[0],menitoff[1],menitoff[2],menitoff[3],menitoff[4],menitoff[5],menitoff[6],menitoff[7])
		
        # Turn ON heater when passing below the minimum temperature
        if (celsius < TEMP):
            mcp.digitalWrite(HEATER, GPIO.LOW)

        # Turn OFF heater when reaching maximum temperature
 #       if (celsius >= TEMP):
  #          mcp.digitalWrite(HEATER, GPIO.HIGH)
            
        #motor dengan sensor temperature
        if int (GPIO.digitalRead(25)) == 1 :

          if (celsius < 29):
              GPIO.pwmWrite(9, 0)

          if (29.0 < celsius < 29.05):
              GPIO.pwmWrite(9, 0.05)
          if (29.05 < celsius < 29.1):
              GPIO.pwmWrite(9, 0.1)

          if (29.1 < celsius < 29.15):
              GPIO.pwmWrite(9, 0.15)
          if (29.15 < celsius < 29.2):
              GPIO.pwmWrite(9, 0.2)

          if (29.2 < celsius < 29.25):
              GPIO.pwmWrite(9, 0.25)
          if (29.25 < celsius < 29.3):
              GPIO.pwmWrite(9, 0.3)

          if (29.3 < celsius < 29.35):
              GPIO.pwmWrite(9, 0.35)
          if (29.35 < celsius < 29.4):
              GPIO.pwmWrite(9, 0.4)

          if (29.4 < celsius < 29.45):
              GPIO.pwmWrite(9, 0.45)
          if (29.45 < celsius < 29.5):
              GPIO.pwmWrite(9, 0.5)

          if (29.5 < celsius < 29.55):
              GPIO.pwmWrite(9, 0.55)
          if (29.55 < celsius < 29.6):
              GPIO.pwmWrite(9, 0.6)

          if (29.6 < celsius < 29.65):
              GPIO.pwmWrite(9, 0.65)
          if (29.65 < celsius < 29.7):
              GPIO.pwmWrite(9, 0.7)

          if (29.7 < celsius < 29.75):
              GPIO.pwmWrite(9, 0.75)
          if (29.75 < celsius < 29.8):
              GPIO.pwmWrite(9, 0.8)

          if (29.8 < celsius < 29.85):
              GPIO.pwmWrite(9, 0.85)
          if (29.85 < celsius < 29.99):
              GPIO.pwmWrite(9, 0.9)


          if (celsius >= 30):
              GPIO.pwmWrite(9, 1)



    # retrieve current datetime
    now = datetime.datetime.now()
    if (now.second==0):
        match(auto,jamon,jamoff,meniton,menitoff,mcp,mcp2)

 # setting button Home Away
             
    if int (GPIO.digitalRead(7)) == 1 and int (GPIO.digitalRead(11)) == 0 :
      for x in range(0, 8):
         mcp.digitalWrite(x, GPIO.HIGH)
         mcp2.digitalWrite(x, GPIO.HIGH)
         mcp3.digitalWrite(x, GPIO.HIGH)
    #Away
    elif int (GPIO.digitalRead(11)) == 1 and int (GPIO.digitalRead(7)) == 0:
      for x in range(0, 8):
         mcp.digitalWrite(x, GPIO.LOW)
      for x in range(0, 8):
         mcp2.digitalWrite(x, GPIO.LOW)
         mcp3.digitalWrite(x, GPIO.HIGH)

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


    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    # destroy button Home Away
    GPIO.digitalWrite(7, GPIO.LOW)
    GPIO.digitalWrite(8, GPIO.LOW)
    GPIO.digitalWrite(11, GPIO.LOW)
    GPIO.digitalWrite(17, GPIO.LOW)
    GPIO.digitalWrite(18, GPIO.LOW)
    GPIO.digitalWrite(25, GPIO.LOW)
    GPIO.digitalWrite(27, GPIO.LOW)
    GPIO.setFunction(7, GPIO.IN)
    GPIO.setFunction(8, GPIO.IN)
    GPIO.setFunction(11, GPIO.IN)
    GPIO.setFunction(9, GPIO.IN)
    GPIO.setFunction(10, GPIO.IN)
    GPIO.setFunction(17, GPIO.IN)
    GPIO.setFunction(18, GPIO.IN)
    GPIO.setFunction(25, GPIO.IN)
    GPIO.setFunction(27, GPIO.IN)

    mcp  = webiopi.deviceInstance("mcp")       # retrieve the device named "mcp" in the configuration 
    mcp2 = webiopi.deviceInstance("mcp2")
    mcp3 = webiopi.deviceInstance("mcp3")
    
    
    # Setup mcp LOW
    for x in range(0, 8):
      mcp.digitalWrite(x, GPIO.LOW)

    # Setup mcp2y
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
		


# a simple macro to return heater mode
@webiopi.macro
def getMode():
    if (AUTO):
        return "auto"
    return "manual"


# simple macro to set and return heater mode
@webiopi.macro
def setMode(mode):
    global AUTO
    if (mode == "auto"):
        AUTO = True
    elif (mode == "manual"):
        AUTO = False
    return getMode()


@webiopi.macro
def update():
    global auto
    global jamon
    global jamoff
    global meniton
    global menitoff

    auto = [0,0,0,0,0,0,0,0]
    jamon = [0,0,0,0,0,0,0,0]
    jamoff = [0,0,0,0,0,0,0,0]
    meniton = [0,0,0,0,0,0,0,0]
    menitoff = [0,0,0,0,0,0,0,0]


    db = MySQLdb.connect("localhost","root","cherry","monitoring")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM lampu")
    data=cursor.fetchall()
#    print ("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!!!!!")
    i = 0
    for col in data:
	   auto[i] = col[2]
	   jamon[i] = col[3]
	   meniton[i] = col[4]
	   jamoff[i] = col[5]
	   menitoff[i] = col[6]	
	   i = i+1
    db.close()

#    return auto	
    return "%d;%d;%d;%d;%d;%d;%d;%d" % (auto[0],auto[1],auto[2],auto[3],auto[4],auto[5],auto[6],auto[7])
#    return "%d;%d" % (auto[0],auto[1])





def match(auto,jamon,jamoff,meniton,menitoff,mcp,mcp2):
	now = datetime.datetime.now()
	
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

def initauto(auto,jamon,jamoff,meniton,menitoff,mcp,mcp2):
        db = MySQLdb.connect("localhost","root","cherry","monitoring")
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




