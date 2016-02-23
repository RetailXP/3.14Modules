from .BaseDAO import BaseDAO
from Tables.TableStructs import InventoryInfo

class InventoryDAO(BaseDAO):
	sc_database = "/Users/jeongwonchoi/Desktop/University_of_Waterloo/4YDP/4B/GitHub/3.14Modules/DataBaseAccess/test.db"

	def __init__(self, database=sc_database):
		BaseDAO.__init__(self,
						 database,
						 InventoryInfo.getTableName(),
						 InventoryInfo.getColumnHeaders())