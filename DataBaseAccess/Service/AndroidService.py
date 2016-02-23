from DAO.BarcodeDAO import BarcodeDAO
from DAO.CustomerDAO import CustomerDAO
from DAO.FootwearDesignDAO import FootwearDesignDAO
from DAO.FootwearSelectionDAO import FootwearSelectionDAO
from DAO.InventoryDAO import InventoryDAO
from DAO.VirtualCartDAO import VirtualCartDAO

from Tables.TableStructs import *

class AndroidService:

	# given a barcode list for items to display on the first page of the app,
	# return product names, cost and picture for the items in the received order
	def getFirstPageInfo(self, barcodes):
		barcodeDAO = BarcodeDAO()

		barcodePriKeys 			= list()
		footwearSelectionFks 	= list()
		barcodeColHeader 				= "Barcode"
		footwearSelectionFkColHeader 	= "FootwearSelectionDetailsFk"
		for barcode in barcodes:
			barcodePriKey = barcodeDAO.getPriKeys(barcodeColHeader, barcode)
			barcodePriKeys.append( barcodePriKey )
			footwearSelectionFks.append( barcodeDAO.selectAColumn(footwearSelectionFkColHeader, barcodePriKey) )
		barcodeDAO.commitDb() # is this necessary for the connection not making any changes?


		footwearSelectionDAO = FootwearSelectionDAO()

		footwearDesignFks 	= list()
		pictures 			= list()
		footwearDesignFkColHeader	= "FootwearDesignDetailsFk"
		pictureColHeader			= "Picture"

		for footwearSelectionFk in footwearSelectionFks:
			footwearDesignFks.append( footwearSelectionDAO.selectAColumn(footwearSelectionFk) )
			pictures.append( footwearSelectionDAO.selectAColumn() )