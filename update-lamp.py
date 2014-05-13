#!/usr/bin/env python
import sys
import datetime
import MySQLdb
import time

import os


def updateTimeOn(ruang,jam,menit):
	db = MySQLdb.connect("localhost","root","1214174","monitoring")
	cursor = db.cursor()
	cursor.execute("UPDATE lampu SET jam_on = %d , menit_on = %d WHERE ruang='%s'" %(jam, menit, ruang))
	db.commit()
	db.close()
	return

def updateTimeOff(ruang,jam,menit):
	db = MySQLdb.connect("localhost","root","1214174","monitoring")
	cursor = db.cursor()
	cursor.execute("UPDATE lampu SET jam_off = %d , menit_off = %d WHERE ruang='%s'" %(jam, menit, ruang))
	db.commit()
	db.close()
	return

