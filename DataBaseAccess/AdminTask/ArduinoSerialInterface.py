from SerialConnect import SerialConnect
from MessageStruct import MessageStruct

import time

class ArduinoSerialInterface:

	# sc_macSerialPort = "/dev/tty.usbmodem1451"
	# sc_baudRate      = 9600
	# sc_timeout       = 5	# seconds

	def __init__(self, serialPort="/dev/tty.usbmodem1451", baudRate=9600, timeout=5):
		self.__serialConnector = SerialConnect(serialPort, baudRate, timeout)
		self.__serialConn = self.__serialConnector.getSerialConnection()

		self.__serialConn.reset_input_buffer()


	# return only when ACK is received
	def serialWrite(self, message):
		
		ackMsg = ""
		while True:
			self.__serialConn.write(str.encode(message))
			ackMsg = self.__serialConn.readline()

			# if MessageStruct.cs_ack in ackMsg.decode("utf-8"):
			# 	print(ackMsg.decode("utf-8"))
			# 	break

		# if more than one ACK is received
		self.__serialConn.reset_input_buffer()


	# non-blocking i/o.
	# only reads when some message is available in the serial buffer
	def serialRead(self):

		# time.sleep(1)

		# non-blocking i/o
		if self.__serialConn.in_waiting == 0:
			return 0

		# sanitizing the reading
		# self.__serialConn.reset_input_buffer()
		# msg = self.__serialConn.readline()
		# self.__serialConn.reset_input_buffer()

		# return msg
		return str(self.__serialConn.readline().decode("utf-8") )

	# def serialWrite(self, message):
	# 	# self.__serialConn.write(bytearray(message))
	# 	self.__serialConn.write(str.encode(message))

	# def serialRead(self):
	# 	if self.__serialConn.in_waiting == 0:
	# 		return ""

	# 	return str(self.__serialConn.readline().decode("utf-8") )

	def getWaitingQueueByte(self):
		return self.__serialConn.in_waiting

def main():
	adminTask = ArduinoSerialInterface(serialPort="/dev/tty.usbmodemfa131")
	# adminTask.serialWrite("Message from PI!!!")
	
	print("Hi!")

	# for idx in range (1, 20+1):
	idx = 0
	while idx < 20:
		print("writing:")
		adminTask.serialWrite("P>A")

		while adminTask.getWaitingQueueByte() == 0:
			print("while loop")
			time.sleep(1)

		print("serialRead")
		line = adminTask.serialRead()
		print(line)

		idx += 1

	# idx = 0
	# while idx < 20:
	# 	adminTask.serialWrite("P>A");
	# 	line = adminTask.serialRead();
	# 	if line != 0:
	# 		print( line )
	# 	else:
	# 		idx = idx-1
	# 		print( "not here" )
	# 	idx += 1

# def main():
# 	serInterface = ArduinoSerialInterface(serialPort="/dev/tty.usbmodemfa131")

# 	for idx in range(1, 10+1):
# 		print(str(idx) + ": loop")

# 		serInterface.serialWrite(str(idx) + ": Msg From Pi");
# 		time.sleep(5)

# 		returnMsg = ""
# 		while(serInterface.getWaitingQueueByte() == 0):
# 			pass

# 		returnMsg = serInterface.serialRead()
# 		print(returnMsg)






if __name__ == "__main__":
	main()