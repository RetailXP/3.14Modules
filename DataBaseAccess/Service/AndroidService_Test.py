from Service.AndroidService import AndroidService
from DAO.BarcodeDAO import BarcodeDAO
from .DbConnect import DbConnect


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

def main():
	testGetFirstPageInfo()
	testGetSecondPageInfo()

if __name__ == '__main__':
	main()