from BaseDAO import BaseDAO
import TableStruct

class FootwearDesignDAO(BaseDAO):

	def __init__(self, database):
		super.__init__(self,
					   database,
					   FootwearDesignDetails.sc_tableName,
					   FootwearDesignDetails.sc_columnHeaders)
