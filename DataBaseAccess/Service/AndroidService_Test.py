import sys

from Service.AndroidService import AndroidService
from DAO.BarcodeDAO import BarcodeDAO
from DAO.InventoryDAO import InventoryDAO
from .DbConnect import DbConnect

# def testNumItemsAvailable():
# 	dbConnect = DbConnect(BarcodeDAO.getDbDir())
# 	connector = dbConnect.getConnection()

# 	service = AndroidService()
# 	print(service.numItemsAvailable(connector, "Barcode1"))

def testGetFirstPageInfo():
	dbConnect = DbConnect(BarcodeDAO.getDbDir())
	connector = dbConnect.getConnection()

	service = AndroidService()
	print(sys._getframe().f_code.co_name + ": ")
	print( service.getFirstPageInfo( (1,) ) )
	print( service.getFirstPageInfo( (1, 3) ) )
	print("===================================================")
	print("Testing getFirstPageInfo-------------------complete\n\n\n")

def testGetSecondPageInfo():
	dbConnect = DbConnect(BarcodeDAO.getDbDir())
	connector = dbConnect.getConnection()

	service = AndroidService()
	print(sys._getframe().f_code.co_name + ": ")
	print( service.getSecondPageInfo(1) )
	print( service.getSecondPageInfo(3) )
	print("===================================================")
	print("Testing getSecondPageInfo------------------complete\n\n\n")

def testReserveInventoryIfAvailable():
	dbConnect = DbConnect(InventoryDAO.getDbDir())
	connector = dbConnect.getConnection()

	service = AndroidService()
	print(sys._getframe().f_code.co_name + ": ")
	print( service.reserveInventoryIfAvailable(1, 1, 2) )
	print( service.reserveInventoryIfAvailable(1, 1, 1000) )
	print("===================================================")
	print("Testing reserveInventoryIfAvailable--------complete\n\n\n")



def main():
	# testNumItemsAvailable()
	testGetFirstPageInfo()
	testGetSecondPageInfo()
	testReserveInventoryIfAvailable()

if __name__ == '__main__':
	main()