import sys

from Service.AndroidService import AndroidService
from DAO.BarcodeDAO import BarcodeDAO
from DAO.InventoryDAO import InventoryDAO
from .DbConnect import DbConnect

def testNumItemsAvailable():
	dbConnect = DbConnect(BarcodeDAO.getDbDir())
	connector = dbConnect.getConnection()

	service = AndroidService()
	print(service.numItemsAvailable(1))
	print("===================================================")
	print("Testing numItemsAvailable-------------------complete\n\n\n")

def testGetFirstPageInfo():
	dbConnect = DbConnect(BarcodeDAO.getDbDir())
	connector = dbConnect.getConnection()

	service = AndroidService()
	print(sys._getframe().f_code.co_name + ": ")
	print( service.getFirstPageInfo() )
	print("===================================================")
	print("Testing getFirstPageInfo-------------------complete\n\n\n")

def testGetSecondPageInfo():
	dbConnect = DbConnect(BarcodeDAO.getDbDir())
	connector = dbConnect.getConnection()

	service = AndroidService()
	print(sys._getframe().f_code.co_name + ": ")
	print( service.getSecondPageInfo("Selection1") )
	print( service.getSecondPageInfo("Selection2") )
	print("===================================================")
	print("Testing getSecondPageInfo------------------complete\n\n\n")

def testReserveInventoryIfAvailable():
	dbConnect = DbConnect(InventoryDAO.getDbDir())
	connector = dbConnect.getConnection()

	service = AndroidService()
	print(sys._getframe().f_code.co_name + ": ")
	print( service.reserveInventoryIfAvailable(1, 1, 1) )
	print( service.numItemsAvailable(1) )
	print( service.reserveInventoryIfAvailable(1, 1, 1) )
	print( service.numItemsAvailable(1) )
	print("===================================================")
	print("Testing reserveInventoryIfAvailable--------complete\n\n\n")



def main():
	testNumItemsAvailable()
	testGetFirstPageInfo()
	testGetSecondPageInfo()
	testReserveInventoryIfAvailable()

if __name__ == '__main__':
	main()