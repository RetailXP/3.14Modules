from .DbConnect import DbConnect

from DAO.BarcodeDAO import BarcodeDAO
from DAO.CustomerDAO import CustomerDAO
from DAO.FootwearDesignDAO import FootwearDesignDAO
from DAO.FootwearSelectionDAO import FootwearSelectionDAO
from DAO.InventoryDAO import InventoryDAO
from DAO.VirtualCartDAO import VirtualCartDAO

from Tables.TableStructs import *

class ArduinoService:

	sc_xEncodingValues = (0, 22000, 42000)

	def getLocationBoxAbove(self, inventoryDetailsId):

		dbConnect = DbConnect(InventoryDAO.getDbDir())
		connector = dbConnect.getConnection()

		inventoryDAO = InventoryDAO(connector)
		reservedInv = inventoryDAO.selectAnEntry(inventoryDetailsId)

		itemsOnStack = inventoryDAO.selectEntries("X_index", reservedInv[2])

		x_encoder = reservedInv[4]
		y_encoder = 0

		#if no box at the top, set to 0
		if len(itemsOnStack)-1 != reservedInv[3]:
			for item in itemsOnStack:
				if item[3] == reservedInv[3]+1:
					y_encoder = item[5]
					break

		return [x_encoder, y_encoder] 

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
		print("inventory deleted!!!")


		virtualCartDAO = VirtualCartDAO(connector)

		numItemsForPickup = virtualCartDAO.selectAColumn("NumItemAvailableForPickup", virtualCartRowId)
		virtualCartDAO.update(virtualCartRowId, "NumItemAvailableForPickup", numItemsForPickup+1)

	# determine deposit location
	# [x_index, y_index, x_encoder, y_encoder]
	def getDepositLocation(self):

		dbConnect = DbConnect(InventoryDAO.getDbDir())
		connector = dbConnect.getConnection()


		inventoryDAO = InventoryDAO(connector)
		c_maxXIndex = InventoryInfo.sc_maxXIndex
		c_maxYIndex = InventoryInfo.sc_maxYIndex

		oneStackEntries = list()
		x_idx = 0
		for x_idx in range(0, c_maxXIndex):
			oneStackEntries = inventoryDAO.selectEntries("X_index", x_idx)
			if(len(oneStackEntries) <= c_maxYIndex):
				break

		newXIdx = x_idx
		newYIdx = len(oneStackEntries)
		x_encoder = ArduinoService.sc_xEncodingValues[newXIdx]
		y_encoder = 6700

		# the way stocking works for column 0 is different from column 1 and 2
		if newXIdx != 0 and newYIdx == 2:
			return [newxIdx, newYIdx, x_encoder, 36000]

		# !TODO: CHANGE THIS
		maxBoxSize = InventoryInfo.sc_maxBoxSize

		maxY_encoder = 6700
		if newYIdx > 0:
			for item in oneStackEntries:
				if maxY_encoder < item[5]:
					maxY_encoder = item[5]
			y_encoder = maxY_encoder + maxBoxSize

		return [newXIdx, newYIdx, x_encoder, y_encoder]


	# depositing a box back to the inventory
	def depositInventory(self, barcode, x_index, y_index, x_encoder, y_encoder):
		
		dbConnect = DbConnect(InventoryDAO.getDbDir())
		connector = dbConnect.getConnection()


		barcodeDAO = BarcodeDAO(connector)
		barcodeId = barcodeDAO.getPriKeys("Barcode", barcode)[0]


		inventoryDAO = InventoryDAO(connector)
		entry = (barcodeId, x_index, y_index, x_encoder, y_encoder, 0)
		inventoryDAO.createAnEntry(entry)