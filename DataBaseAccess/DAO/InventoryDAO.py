from .BaseDAO import BaseDAO
from Tables.TableStructs import InventoryInfo

class InventoryDAO(BaseDAO):

	def __init__(self, database):
		BaseDAO.__init__(self,
						 database,
						 InventoryInfo.getTableName(),
						 InventoryInfo.getColumnHeaders())