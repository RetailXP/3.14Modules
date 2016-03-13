from MessageStruct import *

class MessageParser:

	def __init__(self):
		self.msgByte = 0		# variable used for communication
		self.retVal  = 0		# also used for communication

		self.genFunc = self.internalParsing() # generator

	def parseMsg(self, msgByte):
		self.msgByte = msgByte
		self.genFunc.__next__()

		return self.retVal

	def getRetVal(self):
		return self.retVal

	
	def internalParsing(self):

		# start byte
		startByte = self.msgByte
		if startByte != MessageFormat.start:
			raise CorruptMsg("startByte: " + str(startByte))
		self.retVal = [False, startByte]
		yield

		# data length
		dataLen = self.msgByte - 1			# to subtract the msgType byte
		self.retVal = [False, dataLen]
		yield

		# msg type
		msgType = self.msgByte
		self.retVal = [False, msgType]
		if msgType > 0x4:
			raise CorruptMsg("msgType: " + str(msgType))
		yield

		# msg content
		msgContent = list()
		for idx in range(0, dataLen):

			dataByte1 = self.msgByte

			if dataByte1 == MessageFormat.start:
				raise CorruptMsg("Reading startbyte in dataByte")

			# no escape code
			if dataByte1 != MessageFormat.escape:
				msgContent.append(dataByte1)
				self.retVal = [False, dataByte1]
				if idx < dataLen-1:
					yield

			# escape code
			else:
				yield

				dataByte2 = self.msgByte - 0x20

				if dataByte2 != MessageFormat.start and dataByte2 != MessageFormat.escape:
					raise CorruptMsg("Escape code misuse")

				msgContent.append(dataByte2)
				self.retVal = [False, dataByte2]
				if idx < dataLen-1:
					yield

		self.retVal = [True, msgType, msgContent]
		yield

class CorruptMsg(BaseException):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr("MsgParser ERROR: " + self.value)
