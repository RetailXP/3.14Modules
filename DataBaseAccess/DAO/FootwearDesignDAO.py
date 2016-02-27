from .BaseDAO import BaseDAO
from Tables.TableStructs import FootwearDesignDetails

class FootwearDesignDAO(BaseDAO):

	def __init__(self, connection):
		BaseDAO.__init__(self,
						 connection,
						 FootwearDesignDetails.getTableName(),
						 FootwearDesignDetails.getColumnHeaders())
