from .BaseDAO import BaseDAO
from Tables.TableStructs import CustomerInfo

class CustomerDAO(BaseDAO):

	def __init__(self, database):
		BaseDAO.__init__(self,
						 database,
						 CustomerInfo.getTableName(),
						 CustomerInfo.getColumnHeaders())