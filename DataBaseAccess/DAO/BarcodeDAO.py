from .BaseDAO import BaseDAO
from Tables.TableStructs import BarcodeDetails

class BarcodeDAO(BaseDAO):

	def __init__(self, connection):
		BaseDAO.__init__(self,
						 connection,
						 BarcodeDetails.getTableName(),
						 BarcodeDetails.getColumnHeaders())