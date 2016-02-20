import BaseDAO
from Tables.TableStructs import InventoryInfo

class InventoryDAO(BaseDAO):

	def __init__(self, database):
		BaseDAO.__init__(self,
						 database,
						 InventoryInfo.sc_tableName,
						 InventoryInfo.sc_columnHeaders)