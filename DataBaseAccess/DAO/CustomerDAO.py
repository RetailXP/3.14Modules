from .BaseDAO import BaseDAO
from Tables.TableStructs import CustomerInfo

class CustomerDAO(BaseDAO):

	def __init__(self, connection):
		BaseDAO.__init__(self,
						 connection,
						 CustomerInfo.getTableName(),
						 CustomerInfo.getColumnHeaders())