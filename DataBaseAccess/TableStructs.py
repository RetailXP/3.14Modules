import BaseTableStruct

# outlines the schema for each table

class FootwearDesignDetails(BaseTableStruct):

	def __init__(self):

		super.__init__(self)
		self.sc_tableName 		= "FOOTWEAR_DESIGN_DETAILS"
		self.sc_columnHeaders 	= ("FootwearDesignId", "ProductName", "BrandName", "Description", "Cost")

		self.footwearDesignDetailsFk	= None
		self.productName				= None
		self.brandName					= None
		self.description				= None
		self.cost 						= None

class FootwearSelectionDetails(BaseTableStruct):

	def __init__(self):

		super.__init__(self)
		self.sc_tableName 		= "FOOTWEAR_SELECTION_DETAILS"
		self.sc_columnHeaders 	= ("FootwearSelectionId", "FootwearDesignDetailsFk", "Selection", "Picture")

		self.footwearSelectionId		= None
		self.footwearDesignDetailsFk	= None
		self.selection					= None
		self.picture					= None

class BarcodeDetails(BaseTableStruct):

	def __init__(self):

		super.__init__(self)
		self.sc_tableName 		= "BARCODE_DETAILS"
		self.sc_columnHeaders 	= ("BarcodeId", "Barcode", "FootwearSelectionDetailsFk", "US_size", "EUR_size", "UK_size", "Gender")

		self.barcodeId 						= None
		self.barcode 						= None
		self.footwearSelectionDetailsFk 	= None
		self.US_size 						= None
		self.EUR_size 						= None
		self.UK_size						= None
		self.gender 						= None

class InventoryInfo(BaseTableStruct):

	def __init__(self):

		super.__init__(self)
		self.sc_tableName 		= "INVENTORY_INFO"
		self.sc_columnHeaders 	= ("InventoryDetailsId", "BarcodeDetailsFk", "X_index", "Y_index")

		self.inventoryDetailsId 	= None
		self.barcodeDetailsFk 		= None
		self.X_index 				= None
		self.Y_index 				= None

class CustomerInfo(BaseTableStruct):

	def __init__(self):

		super.__init__(self)
		self.sc_tableName 		= "CUSTOMER_INFO"
		self.sc_columnHeaders 	= ("CustomerInfoId", "FirstName", "MiddleName", "LastName", "Address", "PhoneNumber")

		self.customerInfoId 	= None
		self.firstName 			= None
		self.middleName 		= None
		self.lastName 			= None
		self.address 			= None
		self.phoneNumber 		= None

class VirtualCart(BaseTableStruct):

	def __init__(self):

		super.__init__(self)
		self.sc_tableName 		= "VIRTUAL_CART"
		self.sc_columnHeaders 	= ("VirtualCartId", "CustomerInfoFk", "BarcodeDetailsFk", "NumCheckedOut")

		self.virtualCartId 		= None
		self.customerInfoFk 	= None
		self.barcodeDetailsFk 	= None
		self.numCheckout 		= None