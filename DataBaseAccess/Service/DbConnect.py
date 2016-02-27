import sqlite3

# The lifespan of DbConnect matches with FootwearDesignDAO

class DbConnect:

	def __init__(self, database):
		self.__database = database
		self.__conn = sqlite3.connect(database)

	# this is an important part of the DAO design. This destructor guarantees no explicit protocol. This design leverages
	# the OOP design
	def __del__(self):
		self.__conn.commit()
		self.__conn.close()

	def getDatabase(self):
		return self.__database

	def getConnection(self):
		return self.__conn
