from AdminTask.ArduinoComm import ArduinoComm
from AdminTask.MessageFormat import MessageFormat
from Service.AndroidService import AndroidService
from Service.ArduinoService import ArduinoService
import queue
import time

def main():

	tabletService = AndroidService()

	# (True, [inventoryDetailsId, X_index, Y_index, X_encoder, Y_encoder]..., newVirtualCartRowId)
	reservationInfo1 = tabletService.reserveInventoryIfAvailable(1, 1, 1)
	reservationInfo2 = tabletService.reserveInventoryIfAvailable(1, 2, 1)
	depositInfo1 = (MessageFormat.depInv, 1)
	depositInfo2 = (MessageFormat.depInv, 2)

	print(reservationInfo1)
	print(reservationInfo2)


	aQueue = queue.Queue(maxsize=0)

	arduinoComm = ArduinoComm("/dev/tty.usbmodemfa131", baudrate=9600, timeout=None)


	# [ MessageFormat.retInv
	#  (True, 
	#  [inventoryDetailsId, barcodeDetailsFk, X_index, Y_index, X_encoder, Y_encoder, checkoutFlag],
	#  newVirtualCartRowId)
	# ]

	robotService = ArduinoService()
	
	for info in reservationInfo1[1]:
		encAbove = robotService.getLocationBoxAbove(info[0])

		aQueue.put([MessageFormat.retInv, (reservationInfo1[0], list(info)+encAbove, reservationInfo1[2])])
	arduinoComm.enqueue(aQueue)

	time.sleep(5)

	for info in reservationInfo2[1]:
		encAbove = robotService.getLocationBoxAbove(info[0])
		aQueue.put([MessageFormat.retInv, (reservationInfo2[0], list(info)+encAbove, reservationInfo2[2]) ])
	arduinoComm.enqueue(aQueue)

	time.sleep(5)

	aQueue.put(depositInfo1)
	arduinoComm.enqueue(aQueue)

	time.sleep(5)

	aQueue.put(depositInfo2)
	arduinoComm.enqueue(aQueue)


if __name__ == "__main__":
	main()