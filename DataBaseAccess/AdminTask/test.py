import serial
import time


def main():
	ser = serial.Serial('/dev/tty.usbmodem1451', 9600, timeout=5)
	
	for idx in range(1, 10+1):

		print("Starting " + str(idx) + " iteration:")

		print('ser.write(b"P>A msg")')
		ser.write(b"P>A msg")

		print("returnline = ser.readline()")
		returnline = ser.readline()
		ser.reset_input_buffer()
		print("returnline=" + str(returnline))
		print("ser.in_waiting=" + str(ser.in_waiting) + "\n")

		time.sleep(1)

	ser.close()

	# returnline = ""
	# idx = 0
	# while str(returnline).find("P<A") == -1 or str(returnline).find("ACK") == -1:
	# 	print("Starting " + str(idx) + " iteration:")
	# 	idx += 1

	# 	print('ser.write(b"P>A msg")')
	# 	ser.write(b"P>A msg")

	# 	print("returnline = ser.readline()")
	# 	returnline = ser.readline()
	# 	print("returnline=" + str(returnline))
	# 	print("ser.in_waiting=" + str(ser.in_waiting) + "\n")

	# ser.reset_input_buffer()

	# returnline = ""
	# while returnline == 0:
	# 	time.sleep(3)
	# 	returnline = ser.readline()

	# ser.reset_input_buffer()
	# print("returnline: " + returnline + "\n\n")


	# ser.close()


if __name__ == "__main__":
	main()
