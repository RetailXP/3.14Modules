import BarcodeDAO
import TableStructs

class InventoryDAO(BaseDAO):

	def __init__(self, database):
		super.__init__(self,
					   database,
					   CustomerInfo.sc_tableName,
					   CustomerInfo.sc_columnHeaders)