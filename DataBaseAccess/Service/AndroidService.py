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
	def __numItemsAvailable(self, connector, barcode):

		barcodeDAO = BarcodeDAO(connector)
		barcodeColHeader = "Barcode"
		barcodePriKey = barcodeDAO.getPriKeys(barcodeColHeader, barcode)[0]

		inventoryDAO = InventoryDAO(connector)
		barcodeDetailsFkColHeader = "BarcodeDetailsFk"
		checkoutFlagColHeader ="CheckoutFlag"
		numItems = 0

		barcodesInInventory = inventoryDAO.getPriKeys(barcodeDetailsFkColHeader, barcodePriKey)

		for barcodeInInventory in barcodesInInventory:
			if inventoryDAO.selectAColumn(checkoutFlagColHeader, barcodeInInventory) == 0:
				numItems += 1

		return numItems

	# given a barcode list for items to display on the first page of the app,
	# return product names, cost and picture for the items in the received order
	def getFirstPageInfo(self, barcodes):

		dbConnect = DbConnect(BarcodeDAO.getDbDir())
		connector = dbConnect.getConnection()

		barcodeDAO = BarcodeDAO(connector)

		barcodePriKeys 			= list()
		footwearSelectionFks 	= list()
		barcodeColHeader 				= "Barcode"
		footwearSelectionFkColHeader 	= "FootwearSelectionDetailsFk"
		for barcode in barcodes:
			barcodePriKey = barcodeDAO.getPriKeys( barcodeColHeader, barcode )
			barcodePriKeys.append(barcodePriKey[0])
			footwearSelectionFks.append( barcodeDAO.selectAColumn(footwearSelectionFkColHeader, barcodePriKey[0]) )


		footwearSelectionDAO = FootwearSelectionDAO(connector)

		footwearDesignFks 	= list()
		pictures 			= list()
		footwearDesignFkColHeader	= "FootwearDesignDetailsFk"
		pictureColHeader			= "Picture"
		for footwearSelectionPriKey in footwearSelectionFks:
			footwearDesignFks.append( footwearSelectionDAO.selectAColumn(footwearDesignFkColHeader, footwearSelectionPriKey) )
			pictures.append( footwearSelectionDAO.selectAColumn(pictureColHeader, footwearSelectionPriKey) )


		footwearDesignDAO = FootwearDesignDAO(connector)

		productNames 	= list()
		costs			= list()
		productNameColHeader 	= "ProductName"
		costColHeader			= "Cost"
		for footwearDesignPriKey in footwearDesignFks:
			productNames.append( footwearDesignDAO.selectAColumn(productNameColHeader, footwearDesignPriKey) )
			costs.append( footwearDesignDAO.selectAColumn(costColHeader, footwearDesignPriKey) )

		
		firstPageInfo = list()
		for i in range(0, len(barcodes)):
			firstPageInfo.append( (productNames[i], costs[i], pictures[i]) )

		return firstPageInfo


	# given a barcode for one item to display on the second page of the app,
	# return Product name, brand name, description, cost, picture, gender, size, availability
	def getSecondPageInfo(self, barcode):

		dbConnect = DbConnect(BarcodeDAO.getDbDir())
		connector = dbConnect.getConnection()


		barcodeDAO = BarcodeDAO(connector)

		barcodePriKey 			= barcodeDAO.getPriKeys("Barcode", barcode)[0]
		footwearSelectionFk 	= barcodeDAO.selectAColumn("FootwearSelectionDetailsFk", barcodePriKey)
		usSize 					= barcodeDAO.selectAColumn("US_size", barcodePriKey)
		eurSize 				= barcodeDAO.selectAColumn("EUR_size", barcodePriKey)
		ukSize 					= barcodeDAO.selectAColumn("UK_size", barcodePriKey)
		gender 					= barcodeDAO.selectAColumn("Gender", barcodePriKey)


		footwearSelectionDAO = FootwearSelectionDAO(connector)

		footwearDesignFk 	= footwearSelectionDAO.selectAColumn("FootwearDesignDetailsFk", footwearSelectionFk)
		picture 			= footwearSelectionDAO.selectAColumn("Picture", footwearSelectionFk)


		footwearDesignDAO = FootwearDesignDAO(connector)

		productName 	= footwearDesignDAO.selectAColumn("ProductName", footwearDesignFk)
		brandName 		= footwearDesignDAO.selectAColumn("BrandName", footwearDesignFk)
		description 	= footwearDesignDAO.selectAColumn("Description", footwearDesignFk)
		cost 			= footwearDesignDAO.selectAColumn("Cost", footwearDesignFk)


		numInventory = self.__numItemsAvailable(connector, barcode)

		return (productName, brandName, description, cost, picture, gender, usSize, eurSize, ukSize, numInventory)


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

	# called when an inventory is retrieved by the robot
	# update the y_encoder and y_index of the affected rows in the InventoryInfoTable
	# delete the respective row in the InventoryInfo table
	# update the respective row in the VirtualCart table
	def processRetrievedInventory(self, inventoryInfoRowId, virtualCartRowId):

		dbConnect = DbConnect(InventoryDAO.getDbDir())
		connector = dbConnect.getConnection()


		# TODO: after debugging this code is done, there should be a check ensuring that there exists
		# such ids

		inventoryDAO = InventoryDAO(connector)
		yIdxColHeader = "Y_index"

		retrievedItemYIndex = inventoryDAO.selectAColumn(yIdxColHeader, inventoryInfoRowId)

		# if the retrieved box is at the top, no need to do updates on y_encoders and y_index
		if retrievedItemYIndex != inventoryDAO.selectMax(yIdxColHeader):
			idBoxAbove = inventoryDAO.getPriKeys(yIdxColHeader, retrievedItemYIndex+1)[0]

			yEncoderColHeader = "Y_encoder"
			encoderOffset = (inventoryDAO.selectAColumn(yEncoderColHeader, idBoxAbove) - 
							 inventoryDAO.selectAColumn(yEncoderColHeader, inventoryInfoRowId))
			
			# update the y_encoder and y_index values for the boxes above the retrieved box
			xIdxColHeader = "X_index"
			retrievedItemXIdx = inventoryDAO.selectAColumn(xIdxColHeader, inventoryInfoRowId)
			sameStackItemIds = inventoryDAO.getPriKeys(xIdxColHeader, retrievedItemXIdx)
			for sameStackItemId in sameStackItemIds:
				curYIdx = inventoryDAO.selectAColumn(yIdxColHeader, sameStackItemId)

				if curYIdx > retrievedItemYIndex:
					inventoryDAO.update(sameStackItemId, yIdxColHeader, curYIdx-1)

					curYEncoder = inventoryDAO.selectAColumn(yEncoderColHeader, sameStackItemId)
					inventoryDAO.update(sameStackItemId, yEncoderColHeader, curYEncoder-encoderOffset)

		inventoryDAO.delete(inventoryInfoRowId)


		virtualCartDAO = VirtualCartDAO(connector)

		numItemsForPickup = virtualCartDAO.selectAColumn("NumItemAvailableForPickup", virtualCartRowId)
		virtualCartDAO.update(virtualCartRowId, "NumItemAvailableForPickup", numItemsForPickup+1)


	# depositing a box back to the inventory
	def depositInventory(self, barcode, x_index, y_index, x_encoder, y_encoder):
		
		dbConnect - DbConnect(InventoryDAO.getDbDir())
		connector = dbConnect.getConnection()


		barcodeDAO = BarcodeDAO(connector)
		barcodeId = barcodeDAO.selectAColumn("BarcodeId", barcode)


		inventoryDAO = InventoryDAO(connector)
		entry = (barcodeId, x_index, y_index, x_encoder, y_encoder, 0)
		inventoryDAO.createAnEntry(entry)
