import BaseDAO
from Tables.TableStructs import VirtualCart

class BarcodeDAO(BaseDAO):

	def __init__(self, database):
		BaseDAO.__init__(self,
						 database,
						 VirtualCart.sc_tableName,
						 VirtualCart.sc_columnHeaders)