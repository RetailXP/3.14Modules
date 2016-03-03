import serial


def main():
	ser = serial.Serial('/dev/tty.usbmodemfa131', 9600)
	# ser.open()
	
	while True:
		print(ser.readline())

	ser.close()


if __name__ == "__main__":
	main()