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


	# return only when ACK is received
	def serialWrite(self, message):
		
		ackMsg = ""
		while True:
			self.__serialConn.write(str.encode(message))
			ackMsg = self.__serialConn.readline()

			if MessageStruct.cs_ack in ackMsg.decode("utf-8"):
				print(ackMsg.decode("utf-8"))
				break

		# if more than one ACK is received
		self.__serialConn.reset_input_buffer()


	# non-blocking i/o.
	# only reads when some message is available in the serial buffer
	def serialRead(self):

		time.sleep(10)

		# non-blocking i/o
		if self.__serialConn.in_waiting == 0:
			# print("in if")
			return ""

		# sanitizing the reading
		self.__serialConn.reset_input_buffer()
		msg = self.__serialConn.readline()
		self.__serialConn.reset_input_buffer()

		return msg

def main():
	adminTask = ArduinoSerialInterface()
	adminTask.serialWrite("Message from PI!!!")
	# line = adminTask.serialRead();
	# print( str(line.decode("utf-8")) )


if __name__ == "__main__":
	main()