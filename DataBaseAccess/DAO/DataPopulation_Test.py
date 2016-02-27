from Service.DbConnect import DbConnect

from DAO.BarcodeDAO import BarcodeDAO
from DAO.CustomerDAO import CustomerDAO
from DAO.FootwearDesignDAO import FootwearDesignDAO
from DAO.FootwearSelectionDAO import FootwearSelectionDAO
from DAO.InventoryDAO import InventoryDAO
from DAO.VirtualCartDAO import VirtualCartDAO

from Tables.TableStructs import *

gc_database = "/Users/jeongwonchoi/Desktop/University_of_Waterloo/4YDP/4B/GitHub/3.14Modules/DataBaseAccess/test.db"
gc_dbConnect = DbConnect(gc_database)
gc_connector = gc_dbConnect.getConnection()

def populateFootwearDesignDetails():

	dao = FootwearDesignDAO(gc_connector)

	productName 	= "Shoe"
	brandName   	= "Brand"
	description		= "Description"
	cost			= 1.00

	for i in range(1, 10+1):
		entry = (productName+str(i), brandName+str(i), description+str(i), cost)
		dao.createAnEntry(entry)

		cost += 1

	# dao.commitDb()
	print(dao.selectAllEntries())

def populateFootwearSelectionDetails():

	dao = FootwearSelectionDAO(gc_connector)

	footwearDesignDetailsFk = 1
	selection = "Selection"
	selectionNum = 1

	for i in range(1, 20+1):
		entry = (footwearDesignDetailsFk,
				 selection+str(footwearDesignDetailsFk)+"."+str(selectionNum),
				 None)
		dao.createAnEntry(entry)

		# if index even
		if i%2 == 0:
			footwearDesignDetailsFk += 1
		selectionNum = i%2+1

	# dao.commitDb()
	print(dao.selectAllEntries())

def populateBarcodeDetails():

	dao = BarcodeDAO(gc_connector)

	barcode = "Barcode"
	footwearSelectionDetailsFk = 1
	US_size = 1
	EUR_size = 2
	UK_size = 3
	gender = ("M", "N")

	for i in range(1, 20+1):
		entry = (barcode+str(i),
				 footwearSelectionDetailsFk,
				 US_size,
				 EUR_size,
				 UK_size,
				 gender[i%2])
		dao.createAnEntry(entry)

		footwearSelectionDetailsFk += 1
		US_size += 3
		EUR_size += 3
		UK_size += 3

	# dao.commitDb()
	print(dao.selectAllEntries())

def populateInventoryInfo():

	dao = InventoryDAO(gc_connector)

	for i in range(1, 20+1):
		value = i%20+1
		entry = (value, value, value)

		dao.createAnEntry(entry)

	# dao.commitDb()
	print(dao.selectAllEntries())

def populateCustomerInfo():

	dao = CustomerDAO(gc_connector)

	dao.createAnEntry(("Harry",
					  "James",
					  "Potter",
					  "4 Private Drive, Little Whinging, Surry, England, Great Britain",
					  "44-2001-2011"))
	dao.createAnEntry(("Winston",
					  None,
					  "Smith",
					  "Victory Mansions, London, England, Great Britain",
					  "1984-1984-1984"))

	# dao.commitDb()
	print(dao.selectAllEntries())

def populateVirtualCart():

	dao = VirtualCartDAO(gc_connector)

	dao.createAnEntry( (1, 1, 1, 0) )
	dao.createAnEntry( (1, 2, 2, 0) )
	dao.createAnEntry( (1, 3, 1, 0) )
	dao.createAnEntry( (2, 1, 1, 0) )
	dao.createAnEntry( (2, 2, 1, 0) )
	dao.createAnEntry( (2, 3, 1, 0) )

	# dao.commitDb()
	print(dao.selectAllEntries())

def main():
	populateFootwearDesignDetails()
	populateFootwearSelectionDetails()
	populateBarcodeDetails()
	populateInventoryInfo()
	populateCustomerInfo()
	populateVirtualCart()

	# gc_connector.commit()


if __name__ == "__main__":
	main()