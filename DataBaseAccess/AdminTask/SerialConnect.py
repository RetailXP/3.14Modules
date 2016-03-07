import serial

class SerialConnect:

	def __init__(self, serialPort, baudRate, timeout):
		self.__serialPort = serialPort
		self.__ser = serial.Serial(serialPort, baudRate, timeout=timeout)

	def __del__(self):
		self.__ser.close()

	def getSerialConnection(self):
		return self.__ser