from abc import ABCMeta

class DataAccess(metaclass=ABCMeta):

	@abstractmethod
	def __init__(self, database):
		self.connector = DbAccess(database).getConnection()
		self.cursor = self.connector.cursor()

	@abstractmethod
	def createAnEntry(self, entry):
		pass

	@abstractmethod
	def getAnEntry(self, id):
		pass

	@abstractmethod
	def getAllEntries(self):
		pass

	@abstractmethod
	def delete(self, id):
		pass

	@abstractmethod
	def update(self, id, columnName, newVal):
		pass
