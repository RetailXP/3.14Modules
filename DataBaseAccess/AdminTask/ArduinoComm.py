import serial
import threading
import time
import queue
from AdminTask.MessageParser import *
from AdminTask.MessageFormat import *

from Service.ArduinoService import ArduinoService


class ArduinoComm(threading.Thread):

	# timeout=None causes the serial connection to wait forever
	def __init__(self, serialPort, baudrate, timeout=None):
		threading.Thread.__init__(self)

		self.__ser = serial.Serial(port=serialPort, baudrate=baudrate, timeout=timeout)

		self.msgQueue = queue.Queue(maxsize=0)  # infinite queue size
		self.msgInProcess = None		# msg received	

		self.start()

	def __del__(self):
		self.__ser.close()

	# if a Queue is passed, the passed queue will be empty by the end of this operation
	# the msgQueue format is [msgType, (msgContent)]
	def enqueue(self, queue):
		while not queue.empty():
			self.msgQueue.put(queue.get())

	def run(self):

		time.sleep(5)

		print("Starting!!!")

		while True:

			## sending a message to Arduino
			while self.msgQueue.empty():
				time.sleep(1)	# poll the queue every 1 second
				
			# [ MessageFormat.retInv
			# (True, 
			#  [inventoryDetailsId, barcodeDetailsFk, X_index, Y_index, X_encoder, Y_encoder, checkoutFlag],
			#  newVirtualCartRowId)
			# ]

			# [ MessageFormat.depInv, barcode ]

			msgQueue = self.msgQueue.get()
			msgType = msgQueue[0]
			txMsg = None
			encodedMsg = None

			if msgType == MessageFormat.retInv:
				reservedInventoryLoc = msgQueue[1][1]
				virtCartRowId = msgQueue[1][2]

				txMsg = RetInvP2A()
				txMsg.invInfoRowId = reservedInventoryLoc[0]
				txMsg.virtCartId = virtCartRowId
				txMsg.x_idx = reservedInventoryLoc[1]
				txMsg.y_idx = reservedInventoryLoc[2]
				txMsg.x_enc = reservedInventoryLoc[3]
				txMsg.y_enc = reservedInventoryLoc[4]
				txMsg.x_encAbove = reservedInventoryLoc[5]
				txMsg.y_encAbove = reservedInventoryLoc[6]

				self.msgInProcess = [MessageFormat.retInv, txMsg]

			elif msgType == MessageFormat.depInv:
				barcode = msgQueue[1]

				robotService = ArduinoService()
				[x_idx, y_idx, x_enc, y_enc] = robotService.getDepositLocation()

				txMsg = DepoInvP2A()
				txMsg.barcode = barcode
				txMsg.x_enc = x_enc
				txMsg.y_enc = y_enc

				self.msgInProcess = [MessageFormat.depInv, (barcode, x_idx, y_idx, x_enc, y_enc)]


			try:
				encodedMsg = txMsg.encode()
			except CorruptData as details:
				print(details)


			for byte in encodedMsg:
				print("writing: " + str(hex(byte)))
				self.__ser.write(bytes([byte]))


			## receiving message from arduino
			print("start receiving messages")


			msgParser = MessageParser()

			isCompleteMsg = False
			while not isCompleteMsg:
				msgByte = self.__ser.read(1)		# blocking i/o with infinite timeout
				parseResult = msgParser.parseMsg(msgByte)
				isCompleteMsg = parseResult[0]

				print("parsing Msgs: " + str(hex(msgByte)))

			parseResult = msgParser.getRetVal()		# [True, msgType, msgContent]

			print(parseResult[2])

			msgType = parseResult[1]
			msgContent = parseResult[2]

			try:
				robotService = ArduinoService()

				if msgType == MessageFormat.retInv:
					msg = RetInvA2P()
					msg.decode(msgContent)
					service.processRetrievedInventory(msg.invInfoRowId, msg.virtCartId)

				elif msgType == MessageFormat.depInv:
					msg = DepInvA2P()
					msg.decode(msgContent)
					#(barcode, x_index, y_index, x_encoder, y_encoder):
					txMsgContent = self.msgInProcess[1]
					service.depositInventory(txMsgContent[0],
											 txMsgContent[1],
											 txMsgContent[2],
											 txMsgContent[3],
											 txMsgContent[4])

				elif msgType == MessageFormat.homeRobot:
					msg = HomeRobotA2P()
					msg.decode(msgContent)

				elif msgType == MessageFormat.movRobot:
					msg = MovPosA2P()
					msg.decode(msgContent)

			except CorruptData as details:
				print(details)