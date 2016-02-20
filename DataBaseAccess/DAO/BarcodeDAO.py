import BaseDAO
from Tables.TableStructs import BarcodeDetails

class BarcodeDAO(BaseDAO):

	def __init__(self, database):
		BaseDAO.__init__(self,
						 database,
						 BarcodeDetails.sc_tableName,
						 BarcodeDetails.sc_columnHeaders)