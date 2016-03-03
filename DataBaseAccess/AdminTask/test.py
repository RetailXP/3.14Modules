import serial
import time


def main():
	ser = serial.Serial('/dev/tty.usbmodem1451', 9600, timeout=3)
	
	while True:
		time.sleep(3)
		line = ser.readline()
		print("messageFromArduino: " + str(line))
		ser.write(b"ResponseFromPi")
		
		returnline = ser.readline()
		print("returningMessage  :" + str(returnline))
		print("ser.in_waiting    :" + str(ser.in_waiting) + "\n\n")

	ser.close()


if __name__ == "__main__":
	main()
