from AdminTask.MessageFormat import MessageFormat

class BaseMessage():

	def encode(self, messageContent):
		pass

	def decode(self):
		pass

	# it is assumed that the length of the mask is divisible by a byte
	@staticmethod
	def escapeByte(data, mask):

		dataByte = data & mask

		while mask != 0xFF:
			dataByte = dataByte >> 8
			mask = mask >> 8

		if(dataByte == MessageFormat.start or dataByte == MessageFormat.escape):
			return [MessageFormat.escape, dataByte + 0x20]

		return [dataByte]