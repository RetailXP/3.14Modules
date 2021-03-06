from .BaseDAO import BaseDAO
from Tables.TableStructs import FootwearSelectionDetails

class FootwearSelectionDAO(BaseDAO):

	def __init__(self, connection):
		BaseDAO.__init__(self,
						 connection,
						 FootwearSelectionDetails.getTableName(),
						 FootwearSelectionDetails.getColumnHeaders())