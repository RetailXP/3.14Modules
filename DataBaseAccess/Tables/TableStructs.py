from Tables.BaseTableStruct import BaseTableStruct

# outlines the schema for each table

class FootwearDesignDetails(BaseTableStruct):

	def __init__(self):

		self.footwearDesignDetailsFk	= None
		self.productName				= None
		self.brandName					= None
		self.description				= None
		self.cost 						= None

	@staticmethod
	def getTableName():
		return "FOOTWEAR_DESIGN_DETAILS"

	@staticmethod
	def getColumnHeaders():
		return ("FootwearDesignId", "ProductName", "BrandName", "Description", "Cost")

class FootwearSelectionDetails(BaseTableStruct):

	def __init__(self):

		self.footwearSelectionId		= None
		self.footwearDesignDetailsFk	= None
		self.selection					= None
		self.picture					= None

	@staticmethod
	def getTableName():
		return "FOOTWEAR_SELECTION_DETAILS"

	@staticmethod
	def getColumnHeaders():
		return ("FootwearSelectionId", "FootwearDesignDetailsFk", "Selection", "Picture")

class BarcodeDetails(BaseTableStruct):

	def __init__(self):

		self.barcodeId 						= None
		self.barcode 						= None
		self.footwearSelectionDetailsFk 	= None
		self.US_size 						= None
		self.EUR_size 						= None
		self.UK_size						= None
		self.gender 						= None

	@staticmethod
	def getTableName():
		return "BARCODE_DETAILS"

	@staticmethod
	def getColumnHeaders():
		return ("BarcodeId", "Barcode", "FootwearSelectionDetailsFk", "US_size", "EUR_size", "UK_size", "Gender")

class InventoryInfo(BaseTableStruct):

	def __init__(self):

		BaseTableStruct.__init__(self)

		self.inventoryDetailsId 	= None
		self.barcodeDetailsFk 		= None
		self.X_index 				= None
		self.Y_index 				= None

	@staticmethod
	def getTableName():
		return "INVENTORY_INFO"

	@staticmethod
	def getColumnHeaders():
		return ("InventoryDetailsId", "BarcodeDetailsFk", "X_index", "Y_index")

class CustomerInfo(BaseTableStruct):

	def __init__(self):

		BaseTableStruct.__init__(self)

		self.customerInfoId 	= None
		self.firstName 			= None
		self.middleName 		= None
		self.lastName 			= None
		self.address 			= None
		self.phoneNumber 		= None

	@staticmethod
	def getTableName():
		return "CUSTOMER_INFO"

	@staticmethod
	def getColumnHeaders():
		return ("CustomerInfoId", "FirstName", "MiddleName", "LastName", "Address", "PhoneNumber")

class VirtualCart(BaseTableStruct):

	def __init__(self):

		BaseTableStruct.__init__(self)

		self.virtualCartId 		= None
		self.customerInfoFk 	= None
		self.barcodeDetailsFk 	= None
		self.numCheckout 		= None

	@staticmethod
	def getTableName():
		return "VIRTUAL_CART"

	@staticmethod
	def getColumnHeaders():
		return ("VirtualCartId", "CustomerInfoFk", "BarcodeDetailsFk", "NumCheckedOut")