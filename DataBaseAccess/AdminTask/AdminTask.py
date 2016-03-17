from AdminTask.ArduinoComm import ArduinoComm
from AdminTask.tcpservlet import TCPServlet
from AdminTask.MessageFormat import MessageFormat

from Service.ArduinoService import ArduinoService

import queue
import time
import threading

class AdminTask(threading.Thread):

	def __init__(self):
		self.tabletComm = TCPServlet()
		self.robotComm = ArduinoComm()
		self.msgQueue = queue.Queue(0)  # infinite queue size

		self.start()

	def getMsgFromTablet(self):
		tabletQueue = self.tabletComm.getMsgQueue()
		while not tabletQueue.empty():
			self.msgQueue.put(tabletQueue.get())

	def enqueueToRobot(self):
		while not self.msgQueue.empty():
			msg = self.msgQueue.get()

			if msg[0] == MessageFormat.retInv:
				for info in msg[1]:
					robotService = ArduinoService()
					encAbove = robotService.getLocationBoxAbove(info[0])
					aQueue = queue.Queue(0)
					aQueue.put([MessageFormat.retInv, (msg[0], list(info)+encAbove, msg[2]) ])

					self.robotComm.enqueue(aQueue)

			# [MessageFormat.depInv, barcode]
			elif msg[0] == MessageFormat.depInv:
				aQueue = queue.Queue(0)
				aQueue.put(msg)

				self.robotComm.enqueue(aQueue)

	def main(self):

		while True:
			
			if self.tabletComm.getMsgQueue().empty():
				time.sleep(1)		# poll tablet msgQueue every 1 second
				continue

			self.getMsgFromTablet()
			self.enqueueToRobot()


def main():
	adminTask = AdminTask()

if __name__ == "__main__":
	main()

