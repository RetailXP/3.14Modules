from .DbConnect import DbConnect

from DAO.BarcodeDAO import BarcodeDAO
from DAO.CustomerDAO import CustomerDAO
from DAO.FootwearDesignDAO import FootwearDesignDAO
from DAO.FootwearSelectionDAO import FootwearSelectionDAO
from DAO.InventoryDAO import InventoryDAO
from DAO.VirtualCartDAO import VirtualCartDAO

from Tables.TableStructs import *

class AndroidService:

	# this method is to be used in other public methods. Thus, for the purpose of 
	# one connection per transaction, pass connector as a parameter

	# given a barcode, it should return the number of items that are not reserved
	def numItemsAvailable(self, barcode):
		dbConnect = DbConnect(FootwearSelectionDAO.getDbDir())
		connector = dbConnect.getConnection()

		return self.__numItemsAvailable(connector, barcode)


	def __numItemsAvailable(self, connector, barcode):

		barcodeDAO = BarcodeDAO(connector)
		barcodeColHeader = "Barcode"
		barcodePriKey = barcodeDAO.getPriKeys(barcodeColHeader, barcode)[0]

		inventoryDAO = InventoryDAO(connector)
		numItems = 0

		barcodesInInventory = inventoryDAO.getPriKeys("BarcodeDetailsFk", barcodePriKey)

		for barcodeInInventory in barcodesInInventory:
			if inventoryDAO.selectAColumn("CheckoutFlag", barcodeInInventory) == 0:
				numItems += 1

		return numItems

	# retrieve information for the first page
	# a list of (selection, product name, brand name, description, cost)
	def getFirstPageInfo(self):

		dbConnect = DbConnect(FootwearSelectionDAO.getDbDir())
		connector = dbConnect.getConnection()

		footwearSelectionDAO = FootwearSelectionDAO(connector)

		selections = footwearSelectionDAO.selectDistinct("Selection")

		queryResult = list()
		for selection in selections:

			footwearDesigns = list()

			for entry in footwearSelectionDAO.selectEntries("Selection", selection):
				footwearDesigns.append(entry[1])

			for footwearDesign in footwearDesigns:
				footwearDesignDAO = FootwearDesignDAO(connector)
				entry = footwearDesignDAO.selectAnEntry(footwearDesign)

				queryResult.append((selection, entry[1], entry[2], entry[3], entry[4]))

		return queryResult


	# given a selection for one item, return barcode, size, gender, availability
	def getSecondPageInfo(self, selection):

		dbConnect = DbConnect(FootwearSelectionDAO.getDbDir())
		connector = dbConnect.getConnection()

		footwearSelectionDAO = FootwearSelectionDAO(connector)
		footwearSelectionPriKeys = footwearSelectionDAO.getPriKeys("Selection", selection)

		retVal = list()

		barcodeDAO = BarcodeDAO(connector)
		for footwearSelectionPriKey in footwearSelectionPriKeys:
			entries = barcodeDAO.selectEntries("FootwearSelectionDetailsFk", footwearSelectionPriKey)

			barcodePriKey = entries[0]

			inventoryDAO = InventoryDAO(connector)
			inventories = inventoryDAO.getPriKeys("BarcodeDetailsFk", barcodePriKey)

			for entry in entries:
				retVal.append((entry[1], entry[3], entry[4], entry[5], entry[6], len(inventories) ) )

		return retVal


	# given the customerId, barcode and quantity, check whether the requested number of
	# items (specified by barcode) are available in the inventory. If available, place 
	# order and return (True, [[InventoryDetailsId, X_index, Y_index, X_encoder, Y_encoder], ...], virtualCartRowId)
	# Otherwise, return (False, numAvailableItems)
	def reserveInventoryIfAvailable(self, customerId, barcode, quantity):

		dbConnect = DbConnect(BarcodeDAO.getDbDir())
		connector = dbConnect.getConnection()

		# the customer should order the exact amount. For example if there exists 1 item in the
		# back room and the customer ordered 2 items, then the whole transaction is rejected.
		# if returning false, the available quantity
		numAvailableItem = self.__numItemsAvailable(connector, barcode)
		if numAvailableItem < quantity:
			return (False, numAvailableItem)


		barcodeDAO = BarcodeDAO(connector)
		barcodePriKey = barcodeDAO.getPriKeys("Barcode", barcode)[0]


		inventoryDAO = InventoryDAO(connector)
		inventoryPriKeys = inventoryDAO.getPriKeys("BarcodeDetailsFk", barcodePriKey)


		virtualCartDAO = VirtualCartDAO(connector)
		newVirtualCartRowId = virtualCartDAO.createAnEntry( (customerId, barcodePriKey, quantity, 0) )


		reservedInventoryLoc = list()
		for index in range(0, quantity):
			reservedInventoryId = inventoryPriKeys[index]
			inventoryDAO.update(reservedInventoryId, "CheckoutFlag", 1)

			# [inventoryDetailsId, barcodeDetailsFk, X_index, Y_index, X_encoder, Y_encoder, checkoutFlag]
			entry = inventoryDAO.selectAnEntry(reservedInventoryId)
			reservedInventoryLoc.append(entry[0:1]+entry[2:6]) # omit barcodeDetailsFk and checkoutFlag

		return (True, reservedInventoryLoc, newVirtualCartRowId)
