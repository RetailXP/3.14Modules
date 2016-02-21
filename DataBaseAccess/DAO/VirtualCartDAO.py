from .BaseDAO import BaseDAO
from Tables.TableStructs import VirtualCart

class VirtualCartDAO(BaseDAO):

	def __init__(self, database):
		BaseDAO.__init__(self,
						 database,
						 VirtualCart.getTableName(),
						 VirtualCart.getColumnHeaders())