import TableStruct
import BaseDAO

class BarcodeDAO(BaseDAO):

	def __init__(self, database):
		super.__init__(self,
					   database,
					   BarcodeDetails.sc_tableName,
					   BarcodeDetails.sc_columnHeaders)