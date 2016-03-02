import serial

class USBConnection:

	def __init__(self, serialDir, baudRate):
		self.__serialComm 	= serial.Serial(serialDir, baudRate)

		#use in_waiting property


def main():
	ser = serial.Serial('/dev/cu.usbmodel1451', 9600)


if __name__ == '__main__':
	main()