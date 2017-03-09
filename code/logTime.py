import os
import time
import sqlite3 as mydb

def logTime():
	#format descriptors:
	#Y is like 1985, m is like 10, d is like 25
	#H is like 23, M is like 59, S is like 08
	xdate = time.strftime("%Y-%m-%d")
	xtime = time.strftime("%H-%M-%S")
	#sqlite3 connection
	con = mydb.connect("/home/pi/testTime.db")
	#with statement closes connection automatically when it's done
	with con:
		#cursor object needed to execute queries
		cur = con.cursor()
		#insert date,time into database
		cur.execute("insert into TimeData values(?,?)", (xdate,xtime))
		print "Time logged",xdate,xtime

logTime()
