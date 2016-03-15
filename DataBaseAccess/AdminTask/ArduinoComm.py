import serial
import queue
from AdminTask.MessageParser import *
from AdminTask.MessageFormat import *

from Service.ArduinoService import ArduinoService


class ArduinoComm(Thread):

	# timeout=None causes the serial connection to wait forever
	def __init__(self, serialPort, baudRate, timeout=None):
		Thread.__init__(self)

		self.__ser = serial.Serial(port=serialPort, baudrate=baudrate, timeout=timeout)

		self.msgQueue = queue.Queue(0)  # infinite queue size
		self.msgInProcess = None		# msg received

		self.isWaitingMsg = False		# msg from arduino

		self.start()

	def __del__(self):
		self.__ser.close()

	# if a Queue is passed, the passed queue will be empty by the end of this operation
	# the msgQueue format is [msgType, (msgContent)]
	def enqueue(self, queue):
		while not queue.empty():
			self.msgQueue.put(queue.get())

	def run(self):

		while True:

			## sending a message to Arduino
			if not self.isWaitingMsg and not self.msgQueue.empty():
				
				# [ MessageFormat.retInv
				# (True, 
				#  [inventoryDetailsId, barcodeDetailsFk, X_index, Y_index, X_encoder, Y_encoder, checkoutFlag],
				#  newVirtualCartRowId)
				# ]

				# [ MessageFormat.depInv, barcode ]

				msgQueue = self.msgQueue.get()
				msgType = msgQueue[0]
				msgInProgress = None
				encodedMsg = None

				if msgType == MessageFormat.retInv:
					reservedInventoryLoc = msgQueue[1][1]
					virtCartRowId = msgQueue[1][2]

					msgInProgress = RetInvP2A()
					msgInProgress.invInfoRowId = reservedInventoryLoc[0]
					msgInProgress.virtCartId = virtCartRowId
					msgInProgress.invInfoRowId = reservedInventoryLoc[1]
					msgInProgress.x_idx = reservedInventoryLoc[2]
					msgInProgress.y_idx = reservedInventoryLoc[3]
					msgInProgress.x_enc = reservedInventoryLoc[4]
					msgInProgress.y_enc = reservedInventoryLoc[5]
					msgInProgress.x_encAbove = reservedInventoryLoc[6]
					msgInProgress.y_encAbove = reservedInventoryLoc[7]

					self.msgInProcess = [MessageFormat.retInv, msgInProgress]

				elif msgType == MessageFormat.depInv:
					barcode = msgQueue[1]

					robotService = ArduinoService()
					[x_idx, y_idx, x_enc, y_enc] = robotService.getDepositLocation()

					msgInProgress = DepoInvP2A()
					msgInProgress.barcode = barcode
					msgInProgress.x_enc = x_enc
					msgInProgress.y_enc = y_enc

					self.msgInProcess = [MessageFormat.depInv, (barcode, x_idx, y_idx, x_enc, y_enc)]

				try:
					encodedMsg = msgInProgress.encode()
				except CorruptData as details:
					print(details)

				# send encodedMsg


			## receive the message with blocking i/o
			if self.isWaitingMsg:

				msgParser = MessageParser()
				isCompleteMsg = False

				while not isCompleteMsg:
					msgByte = self.__ser.read(1)		# blocking i/o with infinite timeout
					parseResult = msgParser.parseMsg(msgByte)
					isCompleteMsg = parseResult[0]

				parseResult = msgParser.getRetVal()		# [True, msgType, msgContent]

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
						msgInProgressContent = msgInProgress[1]
						service.depositInventory(msgInProgressContent[0],
												 msgInProgressContent[1],
												 msgInProgressContent[2],
												 msgInProgressContent[3],
												 msgInProgressContent[4])

					elif msgType == MessageFormat.homeRobot:
						msg = HomeRobotA2P()
						msg.decode(msgContent)

					elif msgType == MessageFormat.movRobot:
						msg = MovPosA2P()
						msg.decode(msgContent)

				except CorruptData as details:
					print(details)