import TableStruct
import BaseDAO

#! TODO: make sure the scoping works so that the commit is actually working
#! TODO: consider coming up with a generic basec class for DAO so that the base classes could inherit from it

class FootwearDesignDAO(BaseDAO):

	def __init__(self, database):
		super.__init__(self,
					   database,
					   FootwearDesignDetails.sc_tableName,
					   FootwearDesignDetails.sc_columnHeaders)
