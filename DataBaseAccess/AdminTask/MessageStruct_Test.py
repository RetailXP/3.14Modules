from AdminTask.MessageStruct import *
from AdminTask.MessageParser import *

def testRetInvP2A():

	print("Test1: ")
	c_msg = (0x80, 0x0D, 0x01, 0x01, 0x02, 0x02, 0x05, 0x33, 0x33,
		     0x44, 0x44, 0x55, 0x55, 0x66, 0x66)

	parser = MessageParser()
	for msgByte in c_msg:
		parser.parseMsg(msgByte)

	msgContent = parser.getRetVal()[2]

	data = RetInvP2A()
	data.decode(msgContent)
	data_encode = data.encode()

	print(c_msg)
	print(data_encode)

	# TODO: output the msg content so we can see the data integrity
	print("invInfoRowId: " + str(data.invInfoRowId) )
	print("virtCartId: " + str(data.virtCartId) )
	print("x_idx: " + str(data.x_idx) )
	print("y_idx: " + str(data.y_idx) )
	print("x_enc: " + str(data.x_enc) )
	print("y_enc: " + str(data.y_enc) )
	print("x_encAbove: " + str(data.x_encAbove) )
	print("y_encAbove: " + str(data.y_encAbove) )
	print("\n")


	print("Test2: ")
	c_msg2 = (0x80, 0x0D, 0x01, 0x01, 0x02, 0x03, 0x05, 0x33, 0x33,
		      0x44, 0x44, 0x55, 0x55, 0x66, 0x66)

	parser = MessageParser()
	for msgByte in c_msg2:
		parser.parseMsg(msgByte)

	msgContent2 = parser.getRetVal()[2]
	try:
		data.decode(msgContent2)
	except CorruptData as detail:
		print(detail)


	print("Test3: ")
	c_msg3 = (0x80, 0x0D, 0x01, 0x01, 0x02, 0x02, 0x06, 0x33, 0x33,
		      0x44, 0x44, 0x55, 0x55, 0x66, 0x66)

	parser = MessageParser()
	for msgByte in c_msg3:
		parser.parseMsg(msgByte)

	msgContent3 = parser.getRetVal()[2]

	try:
		data.decode(msgContent3)
	except CorruptData as detail:
		print(detail)
	print("\n")

	print("===================================================")
	print("Testing testRetInvP2A----------------------complete\n\n\n")


def testRetInvA2P():
	
	c_msg = (0x80, 0x2+1, 0x1, 0x1, 0x2)

	parser = MessageParser()
	for msgByte in c_msg:
		parser.parseMsg(msgByte)

	msgContent = parser.getRetVal()[2]

	data = RetInvA2P()
	data.decode(msgContent)

	data_encode = data.encode()

	print("Test1: ")
	print(c_msg)
	print(data_encode)

	print("invInfoRowId: " + str(data.invInfoRowId) )
	print("virtCartId: " + str(data.virtCartId))

	print("===================================================")
	print("Testing RetInvA2P----------------------complete\n\n\n")

def testDepoInvP2A():

	c_msg = (0x80, 0x5+1, 0x2, 0x1, 0x11, 0x11, 0x22, 0x22)
	parser = MessageParser()
	for msgByte in c_msg:
		parser.parseMsg(msgByte)

	msgContent = parser.getRetVal()[2]

	data = DepoInvP2A()
	data.decode(msgContent)

	data_encode = data.encode()

	print("Test1: ")
	print(c_msg)
	print(data_encode)

	print("barcode: " + str(data.barcode))
	print("x_enc: " + str(data.x_enc))
	print("y_enc: " + str(data.y_enc))

	print("===================================================")
	print("Testing DepoInvP2A----------------------complete\n\n\n")


def testDepoInvA2P():
	c_msg = (0x80, 0x3+1, 0x2, 0x1, 0x11, 0x11)
	parser = MessageParser()
	for msgByte in c_msg:
		parser.parseMsg(msgByte)

	msgContent = parser.getRetVal()[2]

	data = DepoInvA2P()
	data.decode(msgContent)

	data_encode = data.encode()

	print("Test1: ")
	print(c_msg)
	print(data_encode)

	print("barcode: " + str(data.barcode))
	print("y_enc: " + str(data.y_enc))

	print("===================================================")
	print("Testing DepoInvA2P----------------------complete\n\n\n")


def testHomeRobotP2A():
	c_msg = (0x80, 0x0+1, 0x3)
	parser = MessageParser()
	for msgByte in c_msg:
		parser.parseMsg(msgByte)

	print(parser.getRetVal())

	msgContent = parser.getRetVal()[2]

	data = HomeRobotP2A()
	data.decode(msgContent)

	data_encode = data.encode()

	print("Test1: ")
	print(c_msg)
	print(data_encode)

	print("===================================================")
	print("Testing HomeRobotP2A----------------------complete\n\n\n")


def testHomeRobotA2P():
	c_msg = (0x80, 0x0+1, 0x3)
	parser = MessageParser()
	for msgByte in c_msg:
		parser.parseMsg(msgByte)

	msgContent = parser.getRetVal()[2]

	data = HomeRobotA2P()
	data.decode(msgContent)

	data_encode = data.encode()

	print("Test1: ")
	print(c_msg)
	print(data_encode)

	print("===================================================")
	print("Testing HomeRobotA2P----------------------complete\n\n\n")


def testMovPosP2A():
	c_msg = (0x80, 0x4+1, 0x4, 0x11, 0x11, 0x22, 0x22)
	parser = MessageParser()
	for msgByte in c_msg:
		parser.parseMsg(msgByte)

	msgContent = parser.getRetVal()[2]

	data = MovPosP2A()
	data.decode(msgContent)

	data_encode = data.encode()

	print("Test1: ")
	print(c_msg)
	print(data_encode)

	print("x_enc: " + str(data.x_enc))
	print("y_enc: " + str(data.y_enc))

	print("===================================================")
	print("Testing MovPosP2A----------------------complete\n\n\n")


def testMovPosA2P():
	print("Test1: ")
	c_msg = (0x80, 0x1+1, 0x4, 0x2)
	parser = MessageParser()
	for msgByte in c_msg:
		parser.parseMsg(msgByte)

	msgContent = parser.getRetVal()[2]

	data = MovPosA2P()
	data.decode(msgContent)

	data_encode = data.encode()

	print(c_msg)
	print(data_encode)
	print("movMode: " + str(data.movMode))
	print("\n")

	print("Test2: ")
	c_msg2 = (0x80, 0x1+1, 0x4, 0x3)
	parser = MessageParser()
	for msgByte in c_msg2:
		parser.parseMsg(msgByte)

	msgContent = parser.getRetVal()[2]

	data = MovPosA2P()
	try:
		data.decode(msgContent)
	except CorruptData as details:
		print(details)

	print("===================================================")
	print("Testing MovPosA2P----------------------complete\n\n\n")



def main():
	testRetInvP2A()
	testRetInvA2P()
	testDepoInvP2A()
	testDepoInvA2P()
	testHomeRobotP2A()
	testHomeRobotA2P()
	testMovPosP2A()
	testMovPosA2P()

if __name__ == "__main__":
	main()