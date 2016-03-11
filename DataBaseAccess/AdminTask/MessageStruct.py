class MessageFormat:

	start 	= 0x80
	escape 	= 0x81

	## header byte (2 bytes)

	# header byte 1 (length of data)
	# header byte 2 (messge type)
	retInv		= 0x1
	depInv 		= 0x2
	homeRobot 	= 0x3
	movRobot	= 0x4


	## message content size (bytes)

	retInvP2A 		= 12
	retInvA2P		= 2

	depoInvP2A		= 5
	depoInvA2P		= 7

	homeRobotP2A	= 0
	homeRobotA2P 	= 0

	movPosP2A 		= 4
	movPosA2P 		= 1

class RetInvP2A:

	# assume correct length for messageContent length
	def __init__(self, messageContent):
		self.invInfoRowId = messageContent[0]
		self.virtCartId = messageContent[1]
		self.x_idx = messageContent[2]
		self.y_idx = messageContent[3]

		self.x_enc = messageContent[4] | messageContent[5] << 8
		self.y_enc = messageContent[6] | messageContent[7] << 8

		self.x_encAbove = messageContent[8] | messageContent[9] << 8
		self.y_encAbove = messageContent[10] | messageContent[11] << 8

class RetInvA2P:

	def __init__(self, messageContent):
		self.invInfoRowId = messageContent[0]
		self.virtCartId = messageContent[1]

class DepoInvP2A:

	def __init__(self, messageContent):
		self.barcode = messageContent[0]
		self.x_enc = messageContent[1] | messageContent[2] << 8
		self.y_enc = messageContent[3] | messageContent[4] << 8

class DepoInvA2P:

	def __init__(self, messageContent):
		self.barcode = messageContent[0]
		self.y_enc = messageContent[1] | messageContent[2] << 8

class MovPosP2A:

	def __init__(self, messageContent):
		self.x_enc = messageContent[0] | messageContent[1] << 8
		self.y_enc = messageContent[2] | messageContent[3] << 8

class MovPosA2P:
	
	cs_dimOOB  	= 0
	cs_movSucc 	= 1
	cs_limitSwi = 2

	def __init__(self, messageContent):
		self.movMode = messageContent[0]

