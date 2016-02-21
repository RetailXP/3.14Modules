from .BaseDAO import BaseDAO
from Tables.TableStructs import FootwearSelectionDetails

class FootwearSelectionDAO(BaseDAO):

	def __init__(self, database):
		BaseDAO.__init__(self,
						 database,
						 FootwearSelectionDetails.getTableName(),
						 FootwearSelectionDetails.getColumnHeaders())