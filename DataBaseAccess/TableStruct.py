# outlines the schema for each table

class FootwearDesignDetails:

	sc_tableName = "FOOTWEAR_DESIGN_DETAILS"
	sc_columnHeaders = ("FootwearDesignId", "ProductName", "BrandName", "Description", "Cost")

	def __init__(self):
		self.footwearDesignDetailsFk	= None
		self.productName				= None
		self.brandName					= None
		self.description				= None
		self.cost 						= None

class FootwearSelectionDetails:

	sc_tableName = "FOOTWEAR_SELECTION_DETAILS"
	sc_columnHeaders = ("FootwearSelectionId", "FootwearDesignDetailsFk", "Selection", "Picture")

	def __init__(self):
		self.footwearSelectionId		= None
		self.footwearDesignDetailsFk	= None
		self.selection					= None
		self.picture					= None

class BarcodeDetails:

	sc_tableName = "BARCODE_DETAILS"
	sc_columnHeaders = ("BarcodeId", "Barcode", "FootwearSelectionDetailsFk", "US_size", "EUR_size", "UK_size", "Gender")

	def __init__(self):
		self.barcodeId 						= None
		self.barcode 						= None
		self.footwearSelectionDetailsFk 	= None
		self.US_size 						= None
		self.EUR_size 						= None
		self.UK_size						= None
		self.gender 						= None

class InventoryInfo:

	sc_tableName = "INVENTORY_INFO"
	sc_columnHeaders = ("InventoryDetailsId", "BarcodeDetailsFk", "X_index", "Y_index")

	def __init__(self):
		self.inventoryDetailsId 	= None
		self.barcodeDetailsFk 		= None
		self.X_index 				= None
		self.Y_index 				= None

class CustomerInfo:

	sc_tableName = "CUSTOMER_INFO"
	sc_columnHeaders = ("CustomerInfoId", "FirstName", "MiddleName", "LastName", "Address", "PhoneNumber")

	def __init__(self):
		self.customerInfoId 	= None
		self.firstName 			= None
		self.middleName 		= None
		self.lastName 			= None
		self.address 			= None
		self.phoneNumber 		= None

class VirtualCart:

	sc_tableName = "VIRTUAL_CART"
	sc_columnHeaders = ("VirtualCartId", "CustomerInfoFk", "BarcodeDetailsFk", "NumCheckedOut")

	def __init__(self):
		self.virtualCartId 		= None
		self.customerInfoFk 	= None
		self.barcodeDetailsFk 	= None
		self.numCheckout 		= None