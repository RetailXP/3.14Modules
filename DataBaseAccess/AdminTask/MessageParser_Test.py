from MessageParser import *

def testCorrectMsgWithoutEscape():
	c_msg = (0x80, 0x4, 0x4, 0x0, 0x1, 0x2, 0x3)

	parser = MessageParser()
	for msgByte in c_msg:
		parser.parseMsg(msgByte)

	print(parser.retVal)

	print("===================================================")
	print("Testing correctMsgWithoutEscape----------------------complete\n\n\n")

def testCorrectMsgWithEscape():
	c_msg = (0x80, 0x6, 0x0, 0x81, 0xA1, 0x81, 0xA0, 0x1, 0x2, 0x3, 0x4)

	parser = MessageParser()
	for msgByte in c_msg:
		print( hex(parser.parseMsg(msgByte)[1]) )

	print(parser.getRetVal())

	print("===================================================")
	print("Testing correctMsgWithEscape----------------------complete\n\n\n")


def testFaultyStartByte():
	c_msg = (0x81, 0x6, 0x0, 0x81, 0xA1, 0x81, 0xA0, 0x1, 0x2, 0x3, 0x4)

	parser = MessageParser()
	
	try:
		for msgByte in c_msg:
			parser.parseMsg(msgByte)

	except CorruptMsg as detail:
		print(detail)

	print("===================================================")
	print("Testing faultyStartByte----------------------complete\n\n\n")

def testFaultyMsgType():
	c_msg = (0x80, 0x6, 0x5, 0x81, 0xA1, 0x81, 0xA0, 0x1, 0x2, 0x3, 0x4)

	parser = MessageParser()
	
	try:
		for msgByte in c_msg:
			parser.parseMsg(msgByte)

	except CorruptMsg as detail:
		print(detail)

	print("===================================================")
	print("Testing faultyMsgType----------------------complete\n\n\n")

def testStartByteWithoutEscape():
	c_msg = (0x80, 0x6, 0x0, 0x80, 0x81)

	parser = MessageParser()
	
	try:
		for msgByte in c_msg:
			parser.parseMsg(msgByte)

	except CorruptMsg as detail:
		print(detail)

	print("===================================================")
	print("Testing startByteWithoutEscape----------------------complete\n\n\n")

def testMisuedEscape():
	c_msg = (0x80, 0x6, 0x0, 0x81, 0x81)

	parser = MessageParser()
	
	try:
		for msgByte in c_msg:
			parser.parseMsg(msgByte)

	except CorruptMsg as detail:
		print(detail)

	print("===================================================")
	print("Testing misuedEscape----------------------complete\n\n\n")

def main():

	testCorrectMsgWithoutEscape()
	testCorrectMsgWithEscape()

	testFaultyStartByte()
	testFaultyMsgType()
	testStartByteWithoutEscape()
	testMisuedEscape()

if __name__ == "__main__":
	main()