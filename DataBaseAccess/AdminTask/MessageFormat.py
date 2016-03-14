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