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

gc_dbConnect = DbConnect("/Users/jeongwon/Desktop/University_of_Waterloo/4YDP/4B/gitdir/3.14Modules/DataBaseAccess/ProductionData.db")
gc_connector = gc_dbConnect.getConnection()

def populateFootwearDesignDetails():

	print(sys._getframe().f_code.co_name + ": ")

	dao = FootwearDesignDAO(gc_connector)

	entries = [
				("HAUGHNEY-70", "Haughney", ".", 69.99),
				("GRADUATE PNL SPM BLK CANVAS", "LACOSTE", ".", 99.99),
				("UA MICRO G ELEVATE", "UNDER ARMOUR", ".", 49.99),
				("FRIDOLPH-27", "FRIDOLPH", ".", 59.99),
				("JACOU-70", "JACOU", ".", 59.00),
				("AGREWIEL-36", "AGREWIEL", ".", 59.99),
				("GRAD VULC TSP US SPM WHT", "LACOSTE", ".", 74.99),
				("GRADUATE PTE SPM DK GRY LTH", "LACOSTE", ".", 99.99),
				("135154", "DEXTER COMFORT", ".", 39.99),
				("25725", "ASHER", ".", 69.99),
				("RW GALA BLK", "ROBERT WAYNE", ".", 120.00),
				("NIKE SB CHECK NB", "NIKE", ".", 90.00)
	          ]


	for entry in entries:
		dao.createAnEntry(entry)

	print(dao.selectAllEntries())

	print("===================================================")
	print("Testing populateFootwearDesignDetails-------------------complete\n\n\n")

def populateFootwearSelectionDetails():

	print(sys._getframe().f_code.co_name + ": ")

	dao = FootwearSelectionDAO(gc_connector)


	selection = "Selection"

	for i in range(1, 12+1):
		entry = (i,
				 selection+str(i),
				 None)
		dao.createAnEntry(entry)

	print(dao.selectAllEntries())

	print("===================================================")
	print("Testing populateFootwearSelectionDetails-------------------complete\n\n\n")

def populateBarcodeDetails():

	print(sys._getframe().f_code.co_name + ": ")

	dao = BarcodeDAO(gc_connector)

	entries = [
				(1, 1, 11, 44.5, 10, "M"),
				(2, 2, 11, 44.5, 10, "M"),
				(3, 3, 12, 46, 11, "M"),
				(4, 4, 11, 44.5, 10, "M"),
				(5, 5, 8, 41, 7.5, "M"),
				(6, 6, 9, 43, 8.5, "M"),
				(7, 7, 12, 46, 11, "M"),
				(8, 8, 11, 44.5, 10, "M"),
				(9, 9, 8.5, 41.5, 8, "M"),
				(10, 10, 9, 43, 8.5, "M"),
				(11, 11, 8, 41, 7.5, "M"),
				(12, 12, 12, 46, 11, "M")
			  ]

	for entry in entries:
		dao.createAnEntry(entry)

	print(dao.selectAllEntries())

	print("===================================================")
	print("Testing populateBarcodeDetails-------------------complete\n\n\n")

def populateInventoryInfo():

	print(sys._getframe().f_code.co_name + ": ")

	dao = InventoryDAO(gc_connector)

	entries = [
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