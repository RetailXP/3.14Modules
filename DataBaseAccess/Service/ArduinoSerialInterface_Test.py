import sys

from ArduinoSerialInterface import ArduinoSerialInterface
from Service.AndroidService import AndroidService
from Service.ArduinoService import ArduinoService
from Service.DbConnect import DbConnect

def testRetrieval():

	tabletService = AndroidService()
	# invLoc = [inventoryDetailsId, X_index, Y_index, X_encoder, Y_encoder]
	[isAvailable, invLoc, vCartRowID] = tabletService.reserveInventoryIfAvailable(self, 1, "Barcode1", 1)


	arduinoComm = ArduinoSerialInterface()
	msg = "P>A"
	for data in invLoc:
		msg = msg + " " + str(data)

	print("msg: " + msg)

	arduinoComm.serialWrite(message)

	while (robotMsg = arduinoComm.serialRead()) == "":
		pass

	print(robotMsg)

	robotService = ArduinoService()
	robotService.processRetrievedInventory()