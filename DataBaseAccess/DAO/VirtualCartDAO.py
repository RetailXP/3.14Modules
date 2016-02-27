from .BaseDAO import BaseDAO
from Tables.TableStructs import VirtualCart

class VirtualCartDAO(BaseDAO):

	def __init__(self, connection):
		BaseDAO.__init__(self,
						 connection,
						 VirtualCart.getTableName(),
						 VirtualCart.getColumnHeaders())