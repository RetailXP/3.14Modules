import TableStruct
import BaseDAO

class BarcodeDAO(BaseDAO):

	def __init__(self, database):
		super.__init__(self,
					   database,
					   VirtualCart.sc_tableName,
					   VirtualCart.sc_columnHeaders)