import BaseDAO
from Tables.TableStructs import CustomerInfo

class InventoryDAO(BaseDAO):

	def __init__(self, database):
		BaseDAO.__init__(self,
						 database,
						 CustomerInfo.sc_tableName,
						 CustomerInfo.sc_columnHeaders)