from AdminTask.BaseMessage import BaseMessage
from AdminTask.MessageFormat import MessageFormat

class RetInvP2A(BaseMessage):

	# assume correct length for messageContent length
	# the member attributes are public, thus is exposed for interfacing
	def __init__(self):
		self.invInfoRowId	= 0
		self.virtCartId		= 0
		self.x_idx			= 0
		self.y_idx			= 0

		self.x_enc 			= 0
		self.y_enc 			= 0

		self.x_encAbove 	= 0
		self.y_encAbove		= 0

	# messageContent is what is returned by the message parser
	def decode(self, messageContent):
		self.invInfoRowId = messageContent[0]
		self.virtCartId = messageContent[1]
		self.x_idx = messageContent[2]
		self.y_idx = messageContent[3]

		self.x_enc = messageContent[4] | messageContent[5] << 8
		self.y_enc = messageContent[6] | messageContent[7] << 8

		self.x_encAbove = messageContent[8] | messageContent[9] << 8
		self.y_encAbove = messageContent[10] | messageContent[11] << 8

		if self.x_idx not in range(0, 3) or self.y_idx not in range(0, 6):
			raise CorruptData("x_idx and y_idx out of bound: (" + str(self.x_idx) + ", " + str(self.y_idx) + ")" )

	def encode(self):
		bitMask = 0xFF

		msg = list()
		msg.append(MessageFormat.start)
		msg.append(MessageFormat.retInvP2A+1)
		msg.append(MessageFormat.retInv)

		msg += RetInvP2A.escapeByte(self.invInfoRowId,  bitMask )
		msg += RetInvP2A.escapeByte(self.virtCartId, bitMask )

		msg += RetInvP2A.escapeByte(self.x_idx, bitMask )
		msg += RetInvP2A.escapeByte(self.y_idx, bitMask )

		msg += RetInvP2A.escapeByte(self.x_enc, bitMask )
		msg += RetInvP2A.escapeByte(self.x_enc, bitMask << 8 )
		msg += RetInvP2A.escapeByte(self.y_enc, bitMask )
		msg += RetInvP2A.escapeByte(self.y_enc, bitMask << 8 )

		msg += RetInvP2A.escapeByte(self.x_encAbove, bitMask )
		msg += RetInvP2A.escapeByte(self.x_encAbove, bitMask << 8 )
		msg += RetInvP2A.escapeByte(self.y_encAbove, bitMask )
		msg += RetInvP2A.escapeByte(self.y_encAbove, bitMask << 8 )

		return msg


class RetInvA2P(BaseMessage):

	def __init__(self):
		self.invInfoRowId = 0
		self.virtCartId = 0

	def decode(self, messageContent):
		self.invInfoRowId = messageContent[0]
		self.virtCartId = messageContent[1]

	def encode(self):
		bitMask = 0xFF

		msg = list()
		msg.append(MessageFormat.start)
		msg.append(MessageFormat.retInvA2P+1)
		msg.append(MessageFormat.retInv)

		msg += RetInvA2P.escapeByte(self.invInfoRowId, bitMask)
		msg += RetInvA2P.escapeByte(self.virtCartId, bitMask)

		return msg

class DepoInvP2A(BaseMessage):

	def __init__(self):
		self.barcode = 0
		self.x_enc = 0
		self.y_enc = 0

	def decode(self, messageContent):
		self.barcode = messageContent[0]
		self.x_enc = messageContent[1] | messageContent[2] << 8
		self.y_enc = messageContent[3] | messageContent[4] << 8

	def encode(self):
		bitMask = 0xFF

		msg = list()
		msg.append(MessageFormat.start)
		msg.append(MessageFormat.depoInvP2A+1)
		msg.append(MessageFormat.depInv)

		msg += DepoInvP2A.escapeByte(self.barcode, bitMask)
		msg += DepoInvP2A.escapeByte(self.x_enc, bitMask)
		msg += DepoInvP2A.escapeByte(self.x_enc, bitMask << 8)
		msg += DepoInvP2A.escapeByte(self.y_enc, bitMask)
		msg += DepoInvP2A.escapeByte(self.y_enc, bitMask << 8)

		return msg

class DepoInvA2P(BaseMessage):

	def __init__(self):
		self.barcode = 0
		self.y_enc = 0

	def decode(self, messageContent):
		self.barcode = messageContent[0]
		self.y_enc = messageContent[1] | messageContent[2] << 8

	def encode(self):
		bitMask = 0xFF

		msg = list()
		msg.append(MessageFormat.start)
		msg.append(MessageFormat.depoInvA2P+1)
		msg.append(MessageFormat.depInv)

		msg += DepoInvA2P.escapeByte(self.barcode, bitMask)
		msg += DepoInvA2P.escapeByte(self.y_enc, bitMask)
		msg += DepoInvA2P.escapeByte(self.y_enc, bitMask << 8)

		return msg

class HomeRobotP2A(BaseMessage):

	def decode(self, messageContent):
		pass

	def encode(self):
		binMask = 0xFF

		msg = list()
		msg.append(MessageFormat.start)
		msg.append(MessageFormat.homeRobotP2A+1)
		msg.append(MessageFormat.homeRobot)

		return msg


class HomeRobotA2P(BaseMessage):

	def decode(self, messageContent):
		pass

	def encode(self):
		bitMask = 0xFF

		msg = list()
		msg.append(MessageFormat.start)
		msg.append(MessageFormat.homeRobotA2P+1)
		msg.append(MessageFormat.homeRobot)

		return msg


class MovPosP2A(BaseMessage):

	def __init__(self):
		self.x_enc = 0
		self.y_enc = 0

	def decode(self, messageContent):
		self.x_enc = messageContent[0] | messageContent[1] << 8
		self.y_enc = messageContent[2] | messageContent[3] << 8

	def encode(self):
		bitMask = 0xFF

		msg = list()
		msg.append(MessageFormat.start)
		msg.append(MessageFormat.movPosP2A+1)
		msg.append(MessageFormat.movRobot)

		msg += MovPosP2A.escapeByte(self.x_enc, bitMask)
		msg += MovPosP2A.escapeByte(self.x_enc, bitMask << 8)
		msg += MovPosP2A.escapeByte(self.y_enc, bitMask)
		msg += MovPosP2A.escapeByte(self.y_enc, bitMask << 8)

		return msg

class MovPosA2P(BaseMessage):
	
	cs_dimOOB  	= 0
	cs_movSucc 	= 1
	cs_limitSwi = 2

	def __init__(self):
		self.movMode = -1

	def decode(self, messageContent):
		self.movMode = messageContent[0]

		if self.movMode not in range(0, 3):
			raise CorruptData("movMode out of bound: " + str(self.movMode))

	def encode(self):
		bitMask = 0xFF

		msg = list()
		msg.append(MessageFormat.start)
		msg.append(MessageFormat.movPosA2P+1)
		msg.append(MessageFormat.movRobot)

		msg += MovPosA2P.escapeByte(self.movMode, bitMask)

		return msg

class CorruptData(BaseException):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr("CorruptData ERROR: " + self.value)