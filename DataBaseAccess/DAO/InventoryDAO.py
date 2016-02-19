import BarcodeDAO
import TableStructs

class InventoryDAO(BaseDAO):

	def __init__(self, database):
		super.__init__(self,
					   database,
					   InventoryInfo.sc_tableName,
					   InventoryInfo.sc_columnHeaders)