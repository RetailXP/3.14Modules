import TableStruct
import BaseDAO

class FootwearSelectionDAO(BaseDAO):

	def __init__(self, database):
		super.__init__(self,
					   database,
					   FootwearSelectionDetails.sc_tableName,
					   FootwearSelectionDetails.sc_columnHeaders)