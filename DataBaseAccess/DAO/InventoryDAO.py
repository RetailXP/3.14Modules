from .BaseDAO import BaseDAO
from Tables.TableStructs import InventoryInfo

class InventoryDAO(BaseDAO):

	def __init__(self, connection):
		BaseDAO.__init__(self,
						 connection,
						 InventoryInfo.getTableName(),
						 InventoryInfo.getColumnHeaders())