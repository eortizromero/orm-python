# -*- coding: utf-8 -*-

import urlparse
import os

try:
	import psycopg2
except ImportError:
	print "Unable to found python library for connect \
with postgresql, try install it with 'pip install psycopg2'."



# class ConfigManager(object):
# 	def __init__(self, fname=None):
# 		self.config_file = fname

# 		self._parse_config()

# 	def _parse_config(self, args=None):
# 		if args is None:
# 			args = []
# 		if os.name == 'nt':

# class Cursor(object):
# 	def __init__(self, pool, dbname, info, serialized=True):
# 		self.__pool = pool
# 		self.dbname = dbname
# 		self._serialized = serialized
# 		self.conex = pool.lend(info)
# 		self._obj = self.conex.cursor()

# class PsycoConnection(psycopg2.extensions.connection):
# 	pass


# def reverse_enum(l):
# 	return izip(xrange(len(l)-1, -1, -1), reversed(l))


# class ConnectionPool(object):
# 	def __init__(self, con_max=64):
# 		self._connections = []
# 		self._con_max = max(con_max, 1)

# 	def __repr__(self):
# 		used = len(1 for c, u in self._connections[:] if u)
# 		count = len(self._connections)
# 		return "ConnectionPool(used=%d/count=%d/max=%d)" %(used, count, self._con_max)

# 	@locked
# 	def lend(self, conn_info):
# 		# for i, (conex, _) in reverse_enum(self._connections):
# 		try:
# 			con = psycopg2.connect(connection_factory\
# 				=PsycoConnection, **conn_info)
# 		except:
# 			print "Unable to connect to database"
# 			raise
# 		self._connections.append((con, True))
# 		print "New connection created!"
# 		return con

# class Connection(object):
# 	def __init__(self, pool, dbname, info):
# 		self.dbname = dbname
# 		self.info = info
# 		self.__pool = pool

# 		def cursor(self, serialized=True):
# 			c_type = serialized and 'serialized' or ''
# 			print "Cursor%s creado para %r", c_type, \
# 			self.info

# 			return Cursor(self.__pool, self.dbname, \
# 				self.info, serialized=serialized)

# def connection_info_for(db_for):
# 	if db_for.startswith(('postgresql://', 'postgres://')):
# 		us = urlparse.urlsplit(db_for)
# 		if len(us.path) > 1:
# 			db_name = us.path[1:]
# 		elif us.username:
# 			db_name = us.username
# 		else:
# 			db_name = us.hostname
# 		return db_name, {'info': db_for}

# 	connection_info = {'database': db_for}
# 	for p in ('host', 'port', 'user', 'password'):
# 		cfg = \

def connect_db():
	try:
		con = psycopg2.connect("dbname='ormdatabase' \
			user='ormusr' \
			host='localhost' \
			password='ormusr'")
	except:
		print "Unable to connect to database"

	cur = con.cursor()

	return cur

	# cur.execute("""SELECT datname FROM pg_database""")

	# rows = cur.fetchall()

	# print "\nShow me databases: \n"

	# name = 'ormdatabase'

	# for row in rows:
	# 	print "  >", row[0]

	# if name in row:
	# 	print "\nDatabase (%s) already exists!\n" % name
	# else:
	# 	print "\nDatabase (%s) doesn't exists, try create it.\n" % name