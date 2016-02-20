import BaseDAO
from Tables.TableStructs import FootwearDesignDetails

class FootwearDesignDAO(BaseDAO):

	def __init__(self, database):
		BaseDAO.__init__(self,
						 database,
						 FootwearDesignDetails.sc_tableName,
						 FootwearDesignDetails.sc_columnHeaders)
