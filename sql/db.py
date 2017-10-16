# -*- coding: utf-8 -*-

import urlparse
import os

try:
	import psycopg2
except ImportError:
	print "Unable to found python library for connect \
with postgresql, try install it with 'pip install psycopg2'."

def connect_db():
	try:
		con = psycopg2.connect("dbname='ormdatabase' \
			user='ormusr' \
			host='localhost' \
			password='ormusr'")
		cur = con.cursor()

		return cur
	except:
		print "Unable to connect to database"