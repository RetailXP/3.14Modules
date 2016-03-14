class BaseDAO:

	# to be overloaded
	@staticmethod
	def getDbDir():
		# return "/Users/jeongwonchoi/Desktop/University_of_Waterloo/4YDP/4B/GitHub/3.14Modules/DataBaseAccess/test.db"
		return "/Users/jeongwon/Desktop/University_of_Waterloo/4YDP/4B/gitdir/3.14Modules/DataBaseAccess/test.db"

	def __init__(self, connection, tableName, columnHeaders):
		self.__connector 		= connection
		self.__cursor 			= self.__connector.cursor()
		self.__tableName 		= tableName
		self.__columnHeaders 	= columnHeaders

	# given a column header and a column value, return a list of corresponding primary keys
	def getPriKeys(self, colHeader, columnValue):
		script = "SELECT " + self.__columnHeaders[0] + " FROM " + self.__tableName +  " WHERE " + colHeader + "=?"

		self.__cursor.execute(script, (str(columnValue), ) )

		queriedRows = self.__cursor.fetchall()

		priKeys = list()
		for row in queriedRows:
			priKeys.append(row[0])
		
		return priKeys

	# assume that the entry is a tuple corresponding to one whole row in a table
	def createAnEntry(self, entry):
		valuePlaceHolders = "("

		# primary key need not be included in the "INSERT INTO ..." script.
		# Thus, the __columnHeaders starts from the second index
		for header in self.__columnHeaders[1:]:
			valuePlaceHolders += "?,"
		valuePlaceHolders = valuePlaceHolders[:-1] + ")" # remove the last comma

		script = "INSERT INTO " + self.__tableName + " " + str(self.__columnHeaders[1:]) + " VALUES " + valuePlaceHolders

		self.__cursor.execute(script, entry)
		return self.__cursor.lastrowid

	# return an entire row from a table using the primary key - id
	def selectAnEntry(self, id):
		script = "SELECT * FROM " + self.__tableName + " WHERE " + self.__columnHeaders[0] + "=?"

		self.__cursor.execute(script, (str(id), ) )

		return self.__cursor.fetchone()

	# given a primary key - id - return values under a column as a list
	def selectAColumn(self, colHeader, id):
		script = "SELECT " + colHeader + " FROM " + self.__tableName + " WHERE " + self.__columnHeaders[0] + "=?"

		self.__cursor.execute(script, (str(id), ) )

		return self.__cursor.fetchone()[0]

	# given a column value, return all rows
	def selectEntries(self, colHeader, val):
		script = "SELECT * FROM " + self.__tableName + " WHERE " + colHeader + "=?"
		self.__cursor.execute(script, (str(val), ) )

		return self.__cursor.fetchall()

	# return the whole table
	def selectAllEntries(self):
		script = "SELECT * FROM " + self.__tableName
		self.__cursor.execute(script)

		return self.__cursor.fetchall()

	def selectMax(self, columnHeader):
		script = 'SELECT max(' + str(columnHeader) + ') FROM ' + self.__tableName
		self.__cursor.execute(script)

		return self.__cursor.fetchone()[0]

	def selectDistinct(self, columnHeader):
		script = "SELECT DISTINCT " + str(columnHeader) + " FROM " + self.__tableName

		self.__cursor.execute(script)
		distincts = self.__cursor.fetchall()

		retVal = list()
		for distinct in distincts:
			retVal.append(distinct[0])

		return retVal

	def delete(self, id):
		script = "DELETE FROM " + self.__tableName + " WHERE " + self.__columnHeaders[0] + "=?"

		self.__cursor.execute(script, (str(id), ) )

	def update(self, id, columnHeader, newVal):
		script = "UPDATE " + self.__tableName + " SET " + columnHeader + "=?" + " WHERE " + self.__columnHeaders[0] + "=" + str(id)

		self.__cursor.execute(script, (str(newVal), ) )

	# according to the documentation at https://docs.python.org/2/library/sqlite3.html
	# for the case of database being accessed by multiple connections, 
	# and one of the processes modifies the database, the SQLite database is locked 
	# until that transaction is committed.
	def commitDb(self):
		self.__connector.commit()