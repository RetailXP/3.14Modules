from AdminTask.ArduinoComm import ArduinoComm
from AdminTask.tcpservlet import TCPServlet

import queue
import time
import threading

class AdminTask(threading.Thread):

	def __init__(self):
		self.tabletComm = TCPServlet()
		self.robotComm = ArduinoComm()
		self.msgQueue = queue.Queue(0)  # infinite queue size

		self.start()

	def main(self):

		while True:
			
			if self.tabletComm.getMsgQueue.empty():
				time.sleep(1)		# poll tablet msgQueue every 1 second
				continue

			self.robotComm.enqueue(self.msgQueue)


def main():
	adminTask = AdminTask()

if __name__ == "__main__":
	main()

