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