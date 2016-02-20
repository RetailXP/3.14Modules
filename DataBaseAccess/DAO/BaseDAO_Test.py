from DAO.BaseDAO import BaseDAO
from Tables.TableStructs import FootwearDesignDetails

def main():
	database = "/Users/jeongwon/Desktop/University_of_Waterloo/4YDP/4B/gitdir/3.14Modules/DataBaseAccess/test.db"

	print(FootwearDesignDetails.getTableName())
	print(FootwearDesignDetails.getColumnHeaders())

	tableName = FootwearDesignDetails.getTableName()
	columnHeaders = FootwearDesignDetails.getColumnHeaders()

	baseDAO = BaseDAO(database, tableName, columnHeaders)

	productName 	= "Shoe"
	brandName   	= "Brand"
	description		= "Description"
	cost			= 1.00

	# testing "createAnEntry" method
	for i in range(1, 10+1):
		entry = (productName+str(i), brandName+str(i), description+str(i), cost)
		baseDAO.createAnEntry(entry)
		print("created: " + str(entry))

		cost += 1

	allEntries = baseDAO.selectAllEntries()

	print(allEntries)

	# testing "getPriKeys" method
	priKey = baseDAO.getPriKeys(FootwearDesignDetails.getColumnHeaders()[0], ("1",))
	print(priKey)

	# testing "selectAnEntry" method
	entry = baseDAO.selectAnEntry(FootwearDesignDetails.getColumnHeaders()[0], ("1",))
	print(entry)

	# testing "selectAllEntry" method
	allEntries = baseDAO.selectAllEntries()
	print(allEntries)

	# testing "delete" method
	baseDAO.delete(FootwearDesignDetails.getColumnHeaders()[0], ("1",))
	print(baseDAO.selectAllEntries())

	# testing "update" method
	baseDAO.delete(FootwearDesignDetails.update(FootwearDesignDetails.getColumnHeaders()[0],
												"2",
												FootwearDesignDetails.getColumnHeaders()[0],
												"1"))

if __name__ == "__main__":
	main()