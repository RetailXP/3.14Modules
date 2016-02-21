from .BaseDAO import BaseDAO
from Tables.TableStructs import FootwearDesignDetails

class FootwearDesignDAO(BaseDAO):

	def __init__(self, database):
		BaseDAO.__init__(self,
						 database,
						 FootwearDesignDetails.getTableName(),
						 FootwearDesignDetails.getColumnHeaders())
