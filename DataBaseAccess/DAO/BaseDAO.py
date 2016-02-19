class BaseDAO(Object):

	def __init__(self, database, tableName, columnHeaders):
		self.__connector 		= DbAccess(database).getConnection()
		self.__cursor 			= self.connector.cursor()
		self.__tableName 		= tableName
		self.__columnHeaders 	= columnHeaders

	def getPriKeys(self, priColHeader, colHeader, conditionVal):
		script = "SELECT ? FROM ? WHERE ? = ?"
		self.__cursor.execute(script, priColHeader, self.__columnHeaders, colHeader, conditionVal);
		
		return self.__cursor.fetchall()

	# assume that the entry is a tuple
	def createAnEntry(self, entry):
		valuePlaceHolders = "("
		for header in columnHeaders:
			valuePlaceHolders += "?,"
		valuePlaceHolders = valuePlaceHolders[:-1] + ")" # remove the last comma

		script = "INSERT INTO ? ? VALUES " + valuePlaceHolders

		self.__cursor.execute(script, self.__tableName, self.__columnHeaders, entry)
		self.__connector.commit()

	def selectAnEntry(self, priColHeader, id):
		script = "SELECT * FROM " + self.__tableName + " WHERE " + priColHeader + " = ?"
		self.__cursor.execute(script, id)

		return self.__cursor.fetchone()

	def selectAllEntries(self, priColHeader):
		script = "SELECT * FROM " + self.__tableName + " WHERE " + self.__tableName;
		self.__cursor.execute(script)

		return self.__cursor.fetchall()

	def delete(self, priColHeader, id):
		script = "DELETE FROM " + self.__tableName + " WHERE " + priColHeader + " = ?"

		self.__cursor.execute(script, id)
		self.__connector.commit()

	def update(self, priColHeader, id, columnName, newVal):
		script = "UPDATE ? SET ? = ? WHERE ? = ?"

		self.__cursor.execute(script, tableName, columnName, newVal, priColHeader, id)
		self.__connector.commit()