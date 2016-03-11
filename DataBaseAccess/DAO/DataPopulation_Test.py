import sys

from Service.DbConnect import DbConnect

from DAO.BaseDAO import BaseDAO
from DAO.BarcodeDAO import BarcodeDAO
from DAO.CustomerDAO import CustomerDAO
from DAO.FootwearDesignDAO import FootwearDesignDAO
from DAO.FootwearSelectionDAO import FootwearSelectionDAO
from DAO.InventoryDAO import InventoryDAO
from DAO.VirtualCartDAO import VirtualCartDAO

from Tables.TableStructs import *

gc_dbConnect = DbConnect(BaseDAO.getDbDir())
gc_connector = gc_dbConnect.getConnection()

def populateFootwearDesignDetails():

	print(sys._getframe().f_code.co_name + ": ")

	dao = FootwearDesignDAO(gc_connector)

	productName 	= "Shoe"
	brandName   	= "Brand"
	description		= "Description"
	cost			= 1.00

	for i in range(1, 5+1):
		entry = (productName+str(i), brandName+str(i), description+str(i), cost)
		dao.createAnEntry(entry)

		cost += 1

	print(dao.selectAllEntries())

	print("===================================================")
	print("Testing populateFootwearDesignDetails-------------------complete\n\n\n")

def populateFootwearSelectionDetails():

	print(sys._getframe().f_code.co_name + ": ")

	dao = FootwearSelectionDAO(gc_connector)

	footwearDesignDetailsFk = 1
	selection = "Selection"

	for i in range(1, 10+1):
		entry = (footwearDesignDetailsFk,
				 selection+str(i),
				 None)
		dao.createAnEntry(entry)

		footwearDesignDetailsFk = (i % 5)+1

	print(dao.selectAllEntries())

	print("===================================================")
	print("Testing populateFootwearSelectionDetails-------------------complete\n\n\n")

def populateBarcodeDetails():

	print(sys._getframe().f_code.co_name + ": ")

	dao = BarcodeDAO(gc_connector)

	footwearSelectionDetailsFk = 1
	US_size = 1
	EUR_size = 2
	UK_size = 3
	gender = ("M", "F")

	for i in range(1, 5+1):
		entry = (i,
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

	print(dao.selectAllEntries())

	print("===================================================")
	print("Testing populateBarcodeDetails-------------------complete\n\n\n")

def populateInventoryInfo():

	print(sys._getframe().f_code.co_name + ": ")

	dao = InventoryDAO(gc_connector)

	entries = [
				(1, 0, 0, 50, 0, 0),
				(2, 0, 1, 50, 20, 0),
				(3, 0, 2, 50, 40, 0),
				(4, 0, 3, 50, 60, 0),
				(5, 1, 0, 100, 0, 0),
				(1, 1, 1, 100, 20, 0),
				(2, 2, 0, 150, 0, 0),
				(3, 2, 1, 150, 20, 0),
				(4, 2, 2, 150, 40, 0),
				(5, 2, 3, 150, 60, 0),
				(1, 2, 4, 150, 80, 0),
				(2, 2, 5, 150, 100, 0)
			  ]

	for entry in entries:
		dao.createAnEntry(entry)

	print(dao.selectAllEntries())

	print("===================================================")
	print("Testing populateInventoryInfo-------------------complete\n\n\n")

def populateCustomerInfo():

	print(sys._getframe().f_code.co_name + ": ")

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

	print(dao.selectAllEntries())

	print("===================================================")
	print("Testing populateCustomerInfo-------------------complete\n\n\n")

def populateVirtualCart():

	print(sys._getframe().f_code.co_name + ": ")

	dao = VirtualCartDAO(gc_connector)

	# dao.createAnEntry( (1, 1, 1, 0) )
	# dao.createAnEntry( (1, 2, 2, 0) )
	# dao.createAnEntry( (1, 3, 1, 0) )
	# dao.createAnEntry( (2, 1, 1, 0) )
	# dao.createAnEntry( (2, 2, 1, 0) )
	# dao.createAnEntry( (2, 3, 1, 0) )

	print(dao.selectAllEntries())

	print("===================================================")
	print("Testing populateVirtualCart-------------------complete\n\n\n")

def main():
	populateFootwearDesignDetails()
	populateFootwearSelectionDetails()
	populateBarcodeDetails()
	populateInventoryInfo()
	populateCustomerInfo()
	populateVirtualCart()


if __name__ == "__main__":
	main()