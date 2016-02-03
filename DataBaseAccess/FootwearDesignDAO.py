import TableStruct

#! TODO: make sure the scoping works so that the commit is actually working
#! TODO: consider coming up with a generic basec class for DAO so that the base classes could inherit from it

class FootwearDesignDAO:

	def __init__(self, connector):
		self.__connector = connector.getConnection() # DbConnect
		self.__cursor = self.__connector.cursor()

	def createAnEntry(self, footwearDesignEntry):
		tableName = FootwearDesignDetails.sc_tableName

		entry = (footwearDesignEntry.footwearDesignDetailsFk,
			     footwearDesignEntry.productName,
			     footwearDesignEntry.brandName,
			     footwearDesignEntry.description,
			     footwearDesignEntry.cost)

		columnHeaders = "("
		valuePlaceHolders = "("

		for header in FootwearDesignDetails.sc_columnHeaders:
			columnHeaders += header
			columnHeaders += ","

			valuePlaceHolders += "?,"

		header = header[:-1] # remove the last comma
		header += ")"

		valuePlaceHolders = valuePlaceHolders[:-1] # remove the last comma

		script = "INSERT INTO ? ? VALUES " + valuePlaceHolders

		self.__cursor.execute(script, tableName, header, entry)
		self.__connector.commit()

	def getAnEntry(self, id):
		tableName 		= FootwearDesignDetails.sc_tableName
		priColHeader 	= FootwearDesignDetails.sc_columnHeaders[0]

		script = "SELECT * FROM " + tableName + " WHERE " + priColHeader + " = ?"

		self.__cursor.execute(script, id)
		self.__connector.commit()

	def getAllEntries(self):
		tableName = FootwearDesignDetails.sc_tableName

		script = "SELECT * FROM " + tableName

		self.__cursor.execute(script)
		self.__connector.commit()

	def delete(self, id):
		tableName 		= FootwearDesignDetails.sc_tableName
		priColHeader 	= FootwearDesignDetails.sc_columnHeaders[0]

		script = "DELETE FROM " + tableName + "WHERE " + priColHeader + " = ?"

		self.__cursor.execute(script, id)
		self.__connector.commit()

	def update(self, id, columnName, newVal):
		tableName 		= FootwearDesignDetails.sc_tableName
		priColHeader	= FootwearDesignDetails.sc_columnHeaders[0]

		script = "UPDATE ? SET ? = ? WHERE ? = ?"

		self.__cursor.execute(script, tableName, columnName, newVal, priColHeader, id)
		self.__connector.commit()
