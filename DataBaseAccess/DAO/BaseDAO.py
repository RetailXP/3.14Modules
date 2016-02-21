from .DbConnect import DbConnect

class BaseDAO:

	def __init__(self, database, tableName, columnHeaders):
		self.__dbConnection		= DbConnect(database)
		self.__connector 		= self.__dbConnection.getConnection()
		self.__cursor 			= self.__connector.cursor()
		self.__tableName 		= tableName
		self.__columnHeaders 	= columnHeaders

	def getPriKeys(self, columnHeader, columnValue):
		script = "SELECT " + self.__columnHeaders[0] + " FROM " + self.__tableName +  " WHERE " + columnHeader + "=?"
		self.__cursor.execute(script, columnValue)
		
		return self.__cursor.fetchall()

	# assume that the entry is a tuple
	def createAnEntry(self, entry):
		valuePlaceHolders = "("

		# primary key need not be included in the "INSERT INTO ..." script.
		# Thus, the __columnHeaders starts from the second index
		for header in self.__columnHeaders[1:]:
			valuePlaceHolders += "?,"
		valuePlaceHolders = valuePlaceHolders[:-1] + ")" # remove the last comma

		script = "INSERT INTO " + self.__tableName + str(self.__columnHeaders[1:]) + " VALUES " + valuePlaceHolders

		self.__cursor.execute(script, entry)
		self.__connector.commit()

	def selectAnEntry(self, priColHeader, id):
		script = "SELECT * FROM " + self.__tableName + " WHERE " + priColHeader + "=?"
		self.__cursor.execute(script, id)

		return self.__cursor.fetchone()

	def selectAllEntries(self):
		script = "SELECT * FROM " + self.__tableName
		self.__cursor.execute(script)

		return self.__cursor.fetchall()

	def delete(self, priColHeader, id):
		script = "DELETE FROM " + self.__tableName + " WHERE " + priColHeader + "=?"

		self.__cursor.execute(script, id)
		self.__connector.commit()

	def update(self, id, columnHeader, newVal):
		script = "UPDATE " + self.__tableName + " SET " + columnHeader + "=?" + " WHERE " + self.__columnHeaders[0] + "=" + id

		print(script)

		self.__cursor.execute(script, newVal)
		self.__connector.commit()