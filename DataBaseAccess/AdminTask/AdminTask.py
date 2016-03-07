from SerialConnect import SerialConnect
from MessageStruct import MessageStruct

import time

class AdminTask:

	sc_macSerialPort = "/dev/tty.usbmodem1451"
	sc_baudRate      = 9600
	sc_timeout       = 5	# seconds

	def __init__(self):
		self.__serialConnector = SerialConnect(AdminTask.sc_macSerialPort, AdminTask.sc_baudRate, AdminTask.sc_timeout)
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

		self.__serialConn.reset_input_buffer()

	def serialRead(self):

		time.sleep(5)

		# non-blocking i/o
		if self.__serialConn.in_waiting == 0:
			print("in if")
			return ""

		msg = self.__serialConn.readline()
		self.__serialConn.reset_input_buffer()

		self.__serialConn.write(str.encode("P>A ACK"))

		return msg

def main():
	adminTask = AdminTask()
	# adminTask.serialWrite("Hi")
	line = adminTask.serialRead();
	print( str(line.decode("utf-8")) )


if __name__ == "__main__":
	main()