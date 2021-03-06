from Service.DbConnect import DbConnect

from DAO.BaseDAO import BaseDAO
from Tables.TableStructs import FootwearDesignDetails


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

	priKey = baseDAO.getPriKeys(g_columnHeaders[0], "1")
	print(priKey)

	print("===================================================")
	print("Testing getPriKeys-------------------------complete\n\n\n")

def testSelectAnEntry(baseDAO):

	print("Testing selectAnEntry: ")

	entry = baseDAO.selectAnEntry(1)
	print(entry)

	print("===================================================")
	print("Testing selectAnEntry----------------------complete\n\n\n")

def testSelectAColumn(baseDAO):

	print("Testing selectAColumn: ")

	colHeader = "ProductName"

	colValues = baseDAO.selectAColumn(colHeader, 4)
	print(colValues)

	print("===================================================")
	print("Testing selectAColumn----------------------complete\n\n\n")	


def testSelectAllEntries(baseDAO):

	print("Testing selectAllEntry")

	allEntries = baseDAO.selectAllEntries()
	print(allEntries)

	print("===================================================")
	print("Testing selectAllEntry---------------------complete\n\n\n")

def testSelectMax(baseDAO):

	print("Testing selectMax")

	result = baseDAO.selectMax("Cost")

	print( result )

	print("===================================================")
	print("Testing testSelectMax---------------------complete\n\n\n")	

def testSelectDistinct(baseDAO):

	print("Testing selectDistinct")

	print( baseDAO.selectDistinct("Description") )

	print("===================================================")
	print("Testing testSelectMax---------------------complete\n\n\n")


def testDelete(baseDAO):

	print("Testing delete")

	baseDAO.delete("5")
	print(baseDAO.selectAllEntries())

	baseDAO.createAnEntry( ("Shoe5", "Brand5", "Description5", 5) )

	print("===================================================")
	print("Testing delete-----------------------------complete\n\n\n")


def testUpdate(baseDAO):

	print("Testing Update")

	# testing "update" method
	baseDAO.update(5,
				   "Cost",
				   1)
	print(baseDAO.selectAllEntries())
	baseDAO.update(5,
			   	   "Cost",
			   	   5)

	print("===================================================")
	print("Testing update-----------------------------complete\n\n\n")


def main():

	dbConnect = DbConnect(BaseDAO.getDbDir())
	connector = dbConnect.getConnection()

	baseDAO = BaseDAO(connector, g_tableName, g_columnHeaders)

	# testCreateAnEntry(baseDAO)
	testGetPriKeys(baseDAO)
	testSelectAnEntry(baseDAO)
	testSelectAllEntries(baseDAO)
	testSelectAColumn(baseDAO)
	testSelectMax(baseDAO)
	testSelectDistinct(baseDAO)
	testDelete(baseDAO)
	testUpdate(baseDAO)

if __name__ == "__main__":
	main()