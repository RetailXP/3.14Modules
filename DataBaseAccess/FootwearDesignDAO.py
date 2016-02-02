import TableStruct

#! TODO: make sure the scoping works so that the commit is actually working
#! TODO: consider coming up with a generic basec class for DAO so that the base classes could inherit from it

class FootwearDesignDAO:

	def __init__(self, connector):
		self.__connector = connector.getConnection() # DbConnect
		self.__cursor = self.__connector.cursor()

	def createAnEntry(self, footwearDesignEntry):
		tableName     = footwearDesignEntry.sc_tableName

		entry = (footwearDesignEntry.footwearDesignDetailsFk,
			     footwearDesignEntry.productName,
			     footwearDesignEntry.brandName,
			     footwearDesignEntry.description,
			     footwearDesignEntry.cost)

		columnHeaders = "("
		valuePlaceHolders = "("

		for header in footwearDesignEntry.sc_columnHeaders:
			columnHeaders += header
			columnHeaders += ","

			valuePlaceHolders += "?,"

		header = header[:-1] # remove the last comma
		header += ")"

		valuePlaceHolders = valuePlaceHolders[:-1] # remove the last comma

		script = "INSERT INTO " + tableName + " " + header + " VALUES " + valuePlaceHolders % entry

		self.__cursor.execute(script)

		self.__connector.commit()

	def getAnEntry(self, id):
		pass

	def getAllEntries(self):
		pass

	def delete(self, id):
		pass

	def update(self, footwearDesignEntry):
		pass
