from AdminTask.ArduinoComm import ArduinoComm
from AdminTask.tcpservlet import TCPServlet

import queue

class AdminTask:

	def __init__(self):
		self.tabletComm = TCPServlet()
		self.robotComm = ArduinoComm()
		self.msgQueue = queue.Queue(0)  # infinite queue size

		self.main()

	def main(self):

		while True:
			self.msgQueue.put(self.tabletComm.getMsgQueue())
			if not self.msgQueue.empty():
				self.robotComm.enqueue(self.msgQueue)