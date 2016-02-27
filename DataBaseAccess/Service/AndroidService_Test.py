from Service.AndroidService import AndroidService
from DAO.BarcodeDAO import BarcodeDAO
from .DbConnect import DbConnect

# def testNumItemsAvailable():
# 	dbConnect = DbConnect(BarcodeDAO.getDbDir())
# 	connector = dbConnect.getConnection()

# 	service = AndroidService()
# 	print( service.numItemsAvailable(connector, ("Barcode2",) ) )

def testGetFirstPageInfo():
	dbConnect = DbConnect(BarcodeDAO.getDbDir())
	connector = dbConnect.getConnection()

	service = AndroidService()
	print("testGetFirstPageInfo: ")
	print( service.getFirstPageInfo( ("Barcode1",) ) )
	# print( service.getFirstPageInfo("Barcode1") )
	# print( service.getFirstPageInfo("Barcode2") )

def main():
	testGetFirstPageInfo()

if __name__ == '__main__':
	main()