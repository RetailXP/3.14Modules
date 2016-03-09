import sys

from Service.AndroidService import AndroidService
from Service.ArduinoService import ArduinoService
from DAO.BarcodeDAO import BarcodeDAO
from DAO.InventoryDAO import InventoryDAO
from DAO.VirtualCartDAO import VirtualCartDAO
from .DbConnect import DbConnect

def testProcessRetrievedInventory():
	print(sys._getframe().f_code.co_name + ": ")

	dbConnect = DbConnect(InventoryDAO.getDbDir())
	connector = dbConnect.getConnection()

	customerId = 1
	barcode = "Barcode1"
	quantity = 2

	androidService = AndroidService()
	inventoryReservation = androidService.reserveInventoryIfAvailable(customerId, barcode, quantity)
	print(inventoryReservation) # (True, reservedInventoryLoc, newVirtualCartRowId)


	arduinoService = ArduinoService()
	print( arduinoService.processRetrievedInventory(1, 1) )

	inventoryDAO = InventoryDAO(connector)
	print( inventoryDAO.selectAllEntries() )

	virtualCartDAO = VirtualCartDAO(connector)
	print( virtualCartDAO.selectAllEntries() )

	print("===================================================")
	print("Testing testProcessRetrievedInventory-------------------complete\n\n\n")

def testGetDepositLocation():
	print(sys._getframe().f_code.co_name + ": ")

	dbConnect = DbConnect(InventoryDAO.getDbDir())
	connector = dbConnect.getConnection()

	arduinoService = ArduinoService()

	print(arduinoService.getDepositLocation())

	print("===================================================")
	print("Testing testProcessRetrievedInventory-------------------complete\n\n\n")


def main():
	# testProcessRetrievedInventory()
	testGetDepositLocation()

if __name__ == '__main__':
	main()