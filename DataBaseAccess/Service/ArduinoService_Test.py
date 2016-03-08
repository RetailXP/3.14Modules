import sys

from Service.AndroidService import AndroidService
from DAO.BarcodeDAO import BarcodeDAO
from DAO.InventoryDAO import InventoryDAO
from .DbConnect import DbConnect

def testProcessRetrievedInventory():
	dbConnect = DbConnect(InventoryDAO.getDbDir())
	connector = dbConnect.getConnection()

	service = AndroidService()
	print(sys._getframe().f_code.co_name + ": ")
	print( service.processRetrievedInventory(1, 1) )

def main():
	testReserveInventoryIfAvailable()

if __name__ == '__main__':
	main()