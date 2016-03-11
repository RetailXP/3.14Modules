import sys

from Service.AndroidService import AndroidService
from Service.ArduinoService import ArduinoService
from DAO.BarcodeDAO import BarcodeDAO
from DAO.InventoryDAO import InventoryDAO
from DAO.VirtualCartDAO import VirtualCartDAO
from .DbConnect import DbConnect

def testGetLocationBoxAbove():
	print(sys._getframe().f_code.co_name + ": ")

	dbConnect = DbConnect(InventoryDAO.getDbDir())
	connector = dbConnect.getConnection()

	arduinoService = ArduinoService()

	print(arduinoService.getLocationBoxAbove(1))

	print("===================================================")
	print("Testing testGetLocationBoxAbove-------------------complete\n\n\n")


def testProcessRetrievedInventory():
	print(sys._getframe().f_code.co_name + ": ")

	dbConnect = DbConnect(InventoryDAO.getDbDir())
	connector = dbConnect.getConnection()

	customerId = 1
	barcode = 1
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

def testDepositInventory():
	print(sys._getframe().f_code.co_name + ": ")

	dbConnect = DbConnect(InventoryDAO.getDbDir())
	connector = dbConnect.getConnection()

	arduinoService = ArduinoService()

	[newXIdx, newYIdx, newXEncoder, newYEncoder] = arduinoService.getDepositLocation()
	print([newXIdx, newYIdx, newXEncoder, newYEncoder])

	arduinoService.depositInventory(5, newXIdx, newYIdx, newXEncoder, newYEncoder)

	inventoryDAO = InventoryDAO(connector)
	print(inventoryDAO.selectAllEntries())

	print("===================================================")
	print("Testing testDepositInventory-------------------complete\n\n\n")


def main():
	testGetLocationBoxAbove()
	testProcessRetrievedInventory()
	testGetDepositLocation()
	testDepositInventory()

if __name__ == '__main__':
	main()