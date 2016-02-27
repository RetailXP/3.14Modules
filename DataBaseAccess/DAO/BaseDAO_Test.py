from Service.DbConnect import DbConnect

from DAO.BaseDAO import BaseDAO
from Tables.TableStructs import FootwearDesignDetails

# TODO: test individual methods in different functions

gc_database = "/Users/jeongwonchoi/Desktop/University_of_Waterloo/4YDP/4B/GitHub/3.14Modules/DataBaseAccess/test.db"
g_tableName = FootwearDesignDetails.getTableName()
g_columnHeaders = FootwearDesignDetails.getColumnHeaders()

def testCreateAnEntry(baseDAO):
	
	print("Testing createAnEntry: ")

	productName 	= "Shoe"
	brandName   	= "Brand"
	description		= "Description"
	cost			= 1.00

	for i in range(1, 10+1):
		entry = (productName+str(i), brandName+str(i), description+str(i), cost)
		baseDAO.createAnEntry(entry)
		print("created: " + str(entry))

		cost += 1

	allEntries = baseDAO.selectAllEntries()
	print(allEntries)

	print("===================================================")
	print("Testing createAnEntry----------------------complete\n\n\n")

def testGetPriKeys(baseDAO):

	print("Testing getPriKeys: ")

	priKey = baseDAO.getPriKeys(g_columnHeaders[0],"1")
	print(priKey)

	print("===================================================")
	print("Testing getPriKeys-------------------------complete\n\n\n")

def testSelectAnEntry(baseDAO):

	print("Testing selectAnEntry: ")

	entry = baseDAO.selectAnEntry("1")
	print(entry)

	print("===================================================")
	print("Testing selectAnEntry----------------------complete\n\n\n")


def testSelectAllEntries(baseDAO):

	print("Testing selectAllEntry")

	allEntries = baseDAO.selectAllEntries()
	print(allEntries)

	print("===================================================")
	print("Testing selectAllEntry---------------------complete\n\n\n")

def testDelete(baseDAO):

	print("Testing delete")

	baseDAO.delete("2")
	print(baseDAO.selectAllEntries())

	print("===================================================")
	print("Testing delete-----------------------------complete\n\n\n")


def testUpdate(baseDAO):

	print("Testing Update")

	# testing "update" method
	baseDAO.update("3",
				   FootwearDesignDetails.getColumnHeaders()[0],
				   "1")
	print(baseDAO.selectAllEntries())

	print("===================================================")
	print("Testing delete-----------------------------complete\n\n\n")


def main():

	dbConnect = DbConnect(gc_database)
	connector = dbConnect.getConnection()

	baseDAO = BaseDAO(connector, g_tableName, g_columnHeaders)

	testCreateAnEntry(baseDAO)
	testGetPriKeys(baseDAO)
	testSelectAnEntry(baseDAO)
	testSelectAllEntries(baseDAO)
	testDelete(baseDAO)
	testUpdate(baseDAO)

if __name__ == "__main__":
	main()