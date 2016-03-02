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
	print("testGetFirstPageInfo: ")
	print( service.getFirstPageInfo( ("Barcode1",) ) )
	print( service.getFirstPageInfo( ("Barcode1", "Barcode3") ) )
	print("===================================================")
	print("Testing getFirstPageInfo-------------------complete\n\n\n")

def testGetSecondPageInfo():
	dbConnect = DbConnect(BarcodeDAO.getDbDir())
	connector = dbConnect.getConnection()

	service = AndroidService()
	print("testGetSecondPageInfo: ")
	print( service.getSecondPageInfo("Barcode1") )
	print( service.getSecondPageInfo("Barcode3") )
	print("===================================================")
	print("Testing getSecondPageInfo------------------complete\n\n\n")

def testReserveInventoryIfAvailable():
	dbConnect = DbConnect(InventoryDAO.getDbDir())
	connector = dbConnect.getConnection()

	service = AndroidService()
	print("testReserveInventoryIfAvailable: ")
	print( service.reserveInventoryIfAvailable(1, "Barcode1", 2) )
	print( service.reserveInventoryIfAvailable(1, "Barcode1", 1000) )
	print("===================================================")
	print("Testing reserveInventoryIfAvailable--------complete\n\n\n")

def main():
	# testNumItemsAvailable()
	testGetFirstPageInfo()
	testGetSecondPageInfo()
	testReserveInventoryIfAvailable()

if __name__ == '__main__':
	main()