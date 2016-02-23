from DAO.BaseDAO import BaseDAO
from Tables.TableStructs import FootwearDesignDetails

def main():
	database = "/Users/jeongwonchoi/Desktop/University_of_Waterloo/4YDP/4B/GitHub/3.14Modules/DataBaseAccess/test.db"

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
	priKey = baseDAO.getPriKeys(("1",))
	print(priKey)

	# testing "selectAnEntry" method
	entry = baseDAO.selectAnEntry(("1",))
	print(entry)

	# testing "selectAllEntry" method
	allEntries = baseDAO.selectAllEntries()
	print(allEntries)

	# testing "delete" method
	baseDAO.delete(("1",))
	print(baseDAO.selectAllEntries())

	# testing "update" method
	baseDAO.update("3",
				   FootwearDesignDetails.getColumnHeaders()[0],
				   "1")
	print(baseDAO.selectAllEntries())

if __name__ == "__main__":
	main()