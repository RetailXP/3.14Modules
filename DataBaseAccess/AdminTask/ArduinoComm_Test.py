from AdminTask.ArduinoComm import ArduinoComm
from AdminTask.MessageFormat import MessageFormat
import queue

def main():
	arduinoComm = ArduinoComm("/dev/tty.usbmodemfd121", baudrate=9600, timeout=None)

	aQueue = queue.Queue(maxsize=0)

	# [ MessageFormat.retInv
	#  (True, 
	#  [inventoryDetailsId, barcodeDetailsFk, X_index, Y_index, X_encoder, Y_encoder, checkoutFlag],
	#  newVirtualCartRowId)
	# ]
	aQueue.put([MessageFormat.retInv, [True, (1, 2, 3, 4, 5, 6, 7), 1]])

	arduinoComm.enqueue(aQueue)


if __name__ == "__main__":
	main()