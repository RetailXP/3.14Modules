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
	def __numItemsAvailable(self, connector, barcode):

		barcodeDAO = BarcodeDAO(connector)
		barcodeColHeader = "Barcode"
		barcodePriKeys = barcodeDAO.getPriKeys(barcodeColHeader, barcode)

		inventoryDAO = InventoryDAO(connector)
		barcodeDetailsFkColHeader = "BarcodeDetailsFk"
		numItems = 0

		for barcodePriKey in barcodePriKeys:
			numItems += len( inventoryDAO.getPriKeys(barcodeDetailsFkColHeader, barcodePriKey) )

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

		footwearSelectionFkColHeader 	= "FootwearSelectionDetailsFk"
		barcodeColHeader				= "Barcode"
		usSizeColHeader					= "US_size"
		eurSizeColHeader				= "EUR_size"
		ukSizeColHeader					= "UK_size"
		genderColHeader					= "Gender"

		barcodePriKey 			= barcodeDAO.getPriKeys(barcodeColHeader, barcode)[0]
		footwearSelectionFk 	= barcodeDAO.selectAColumn(footwearSelectionFkColHeader, barcodePriKey)
		usSize 					= barcodeDAO.selectAColumn(usSizeColHeader, barcodePriKey)
		eurSize 				= barcodeDAO.selectAColumn(eurSizeColHeader, barcodePriKey)
		ukSize 					= barcodeDAO.selectAColumn(ukSizeColHeader, barcodePriKey)
		gender 					= barcodeDAO.selectAColumn(genderColHeader, barcodePriKey)


		footwearSelectionDAO = FootwearSelectionDAO(connector)

		footwearDesignFkColHeader	= "FootwearDesignDetailsFk"
		pictureColHeader			= "Picture"

		footwearDesignFk 	= footwearSelectionDAO.selectAColumn(footwearDesignFkColHeader, footwearSelectionFk)
		picture 			= footwearSelectionDAO.selectAColumn(pictureColHeader, footwearSelectionFk)


		footwearDesignDAO = FootwearDesignDAO(connector)

		productNameColHeader 	= "ProductName"
		brandNameColHeader		= "BrandName"
		descriptionColHeader	= "Description"
		costColHeader			= "Cost"

		productName 	= footwearDesignDAO.selectAColumn(productNameColHeader, footwearDesignFk)
		brandName 		= footwearDesignDAO.selectAColumn(brandNameColHeader, footwearDesignFk)
		description 	= footwearDesignDAO.selectAColumn(descriptionColHeader, footwearDesignFk)
		cost 			= footwearDesignDAO.selectAColumn(costColHeader, footwearDesignFk)


		inventoryDAO = InventoryDAO(connector)

		inventoryPriKeyColHeader = "InventoryDetailsId"

		numInventory = self.__numItemsAvailable(connector, barcode)

		return (productName, brandName, description, cost, picture, gender, usSize, eurSize, ukSize, numInventory)


	# given the customerId, barcode and quantity, check whether the requested number of
	# items (specified by barcode) are available in the inventory. If available, place 
	# order and return True
	# Otherwise, return False
	def placeOrder(customerId, barcode, quantity):

		dbConnect = DbConnect(BarcodeDAO.getDbDir())
		connector = dbConnect.getConnection()

		# the customer should order the exact amount. For example if there exists 1 item in the
		# back room and the customer ordered 2 items, then the whole transaction is rejected.
		# if returning false, the available quantity
		numAvailableItem = self.__numItemsAvailable(connector, barcode)
		if numAvailableItem < quantity:
			return (False, numAvailableItem)

		

