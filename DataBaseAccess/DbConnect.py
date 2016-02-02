import sqlit3

# The lifespan of DbConnect matches with FootwearDesignDAO

class DbConnect:

	def __init__(self, database):
		self.__database = database
		self.__conn = sqlite3.connect(database)

	def __del__(self):
		self.__conn.commit()
		self.__conn.close()

	def getConnection(self):
		return self.__conn

	# # when only inserting or only deleting rows on DB
	# def pushToDb(self, script):
	# 	self.cursor.execute(script)
	# 	self.conn.commit()

	# # when running query on the DB without making changes to DB
	# def pullFromDb(self, script):
	# 	self.cursor.execute(script)
	# 	return self.conn.cursor()