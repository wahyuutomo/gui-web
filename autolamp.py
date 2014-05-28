#!/usr/bin/env python

import datetime
import MySQLdb
import time

def select(table):

	db = MySQLdb.connect("localhost","root","1214174","monitoring")
	cursor = db.cursor()
	cursor.execute("SELECT * FROM " + table)
	data=cursor.fetchall()
	db.close()
	return data

def updatetime(auto,jamon,jamoff,meniton,menitoff):
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
	
	return auto,jamon,jamoff,meniton,menitoff

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

def initautodummy(auto,jamon,jamoff,meniton,menitoff):
	now = datetime.datetime.now()
	i = 0
	while (i<4):
		if (auto[i]==1):
			if (jamon[i]<jamoff[i]):
				if ((now.hour>=jamon[i]) and (now.hour<=jamoff[i])):
					if (now.hour==jamon[i]):
						if (now.minute>=meniton[i]):
							print "lampu %d nyala" %i
						else :
							print "lampu %d mati" %i
					elif (now.hour==jamoff[i]):
						if (now.minute<menitoff[i]):
							print "lampu %d nyala" %i
						else :
							print "lampu %d mati" %i
					else:
						print "lampu %d nyala" %i
				else:
					print "lampu %d mati" %i				
					
			elif (jamon[i]>jamoff[i]):
				if ((now.hour>=jamon[i]) or (now.hour<=jamoff[i])):
					if (now.hour==jamon[i]):
						if (now.minute>=meniton[i]):
							print "lampu %d nyala" %i
						else :
							print "lampu %d mati" %i
					elif (now.hour==jamoff[i]):
						if (now.minute<menitoff[i]):
							print "lampu %d nyala" %i
						else :
							print "lampu %d mati" %i
					else:
						print "lampu %d nyala" %i					
				else:
					print "lampu %d mati" %i
					
			elif (jamon[i]==jamoff[i]):
				if (meniton[i]<menitoff[i]):
					if ((now.minute>=meniton[i]) and (now.minute <= menitoff[i])):
						print "lampu %d nyala" %i
					else:
						print "lampu %d mati" %i
				elif (meniton[i]>menitoff[i]):
					if ((now.minute>=meniton[i]) or (now.minute<=menitoff[i])):
						print "lampu %d nyala" %i
					else:
						print "lampu %d mati" %i
				elif (meniton[i] == menitoff[i]):
						print "lampu %d nyala" %i
				else:
					print "lampu %d mati" %i
		else:
			print "lampu %d mati" %i

		if (auto[i+4]==1):
			#print jamon[i+4],jamoff[i+4]
			if (jamon[i+4]<jamoff[i+4]):
				if ((now.hour>=jamon[i+4]) and (now.hour<=jamoff[i+4])):
					if (now.hour==jamon[i+4]):
						if (now.minute>=meniton[i+4]):
							print "lampu %d nyala" %(i+4)
						else :
							print "lampu %d mati" %(i+4)
					elif (now.hour==jamoff[i+4]):
						if (now.minute<menitoff[i+4]):
							print "lampu %d nyala" %(i+4)
						else :
							print "lampu %d mati" %(i+4)
					else:
						print "lampu %d nyala" %(i+4)
				else:
					print "lampu %d mati" %(i+4)
					
			elif (jamon[i+4]>jamoff[i+4]):
				if ((now.hour>=jamon[i+4]) or (now.hour<=jamoff[i+4])):
					if (now.hour==jamon[i+4]):
						if (now.minute>=meniton[i+4]):
							print "lampu %d nyala" %(i+4)
						else :
							print "lampu %d mati" %(i+4)
					elif (now.hour==jamoff[i+4]):
						if (now.minute<menitoff[i+4]):
							print "lampu %d nyala" %(i+4)
						else :
							print "lampu %d mati" %(i+4)
					else:
						print "lampu %d nyala" %(i+4)
				else:
					print "lampu %d mati" %(i+4)
			elif (jamon[i+4]==jamoff[i+4]):
				if (meniton[i+4]<menitoff[i+4]):
					if ((now.minute>=meniton[i+4]) and (now.minute<=menitoff[i+4])):
						print "lampu %d nyala" %(i+4)
					else:
						print "lampu %d mati" %(i+4)
				elif (meniton[i+4]>menitoff[i+4]):
					if ((now.minute>=meniton[i+4]) or (now.minute<=menitoff[i+4])):
						print "lampu %d nyala" %(i+4)
					else:
						print "lampu %d mati" %(i+4)
				elif (meniton[i+4] == menitoff[i+4]):
						print "lampu %d nyala" %(i+4)
				else:
					print "lampu %d mati" %(i+4)
		else:
			print "lampu %d mati" %(i+4)
		i=i+1

	return

data = select ("lampu")

auto = [0,0,0,0,0,0,0,0]
jamon = [0,0,0,0,0,0,0,0]
jamoff = [0,0,0,0,0,0,0,0]
meniton = [0,0,0,0,0,0,0,0]
menitoff = [0,0,0,0,0,0,0,0]

updatetime(auto,jamon,jamoff,meniton,menitoff)
initautodummy(auto,jamon,jamoff,meniton,menitoff)
now = datetime.datetime.now()

#if (now.second==0):
#	match(auto,jamon,jamoff,meniton,menitoff)

i = 0
#print jamon[i+1]

#for i in range (0,7):
#	print "lampu %d on pukul [ %d:%d ] dan off pukul [ %d:%d ] auto = %d"%(i+1, jamon[i+1],meniton[i],jamoff[i],menitoff[i],auto[i])
#	i = i+1

print "jam sekarang %d:%d"% (now.hour,now.minute)

#while True:
#	now = datetime.datetime.now()
#	if ((now.hour == jamon[0]) and (now.minute == meniton[0])):
#		print ("Fucking Asshole!!!")
#		print "jam %d:%d"%(now.hour,now.minute)
#	
#	print("menit cuy")	
#	time.sleep(60)






