# outlines the schema for each table

class FootwearDesignDetailsTable:

	sc_columnHeaders = ("FootwearDesignId", "ProductName", "BrandName", "Description", "Cost")

	def __init__(self):
		self.m_footwearDesignId
		self.m_productName
		self.m_brandName
		self.m_description
		self.m_cost

class FootwearSelectionDetailsTable:

	sc_columnHeaders = ("FootwearSelectionId", "FootwearDesignDetailsFk", "Selection", "Picture")

	def __init__(self):
		self.m_footwearSelectionId
		self.m_footwearDesignDetailsFk
		self.m_selection
		self.m_picture

class BarcodeDetailsTable:

	sc_columnHeaders = ("BarcodeId", "Barcode", "FootwearSelectionDetailsFk", "US_size", "EUR_size", "UK_size", "Gender")

	def __init__(self):
		self.m_barcodeId
		self.m_barcode
		self.m_footwearSelectionDetailsFk
		self.m_US_size
		self.m_EUR_size
		self.m_UK_size
		self.m_gender

class InventoryInfoTable:

	sc_columnHeaders = ("InventoryDetailsId", "BarcodeDetailsFk", "X_index", "Y_index")

	def __init__(self):
		self.m_inventoryDetailsId
		self.m_barcodeDetailsFk
		self.m_X_index
		self.m_Y_index

class CustomerInfoTable:

	sc_columnHeaders = ("CustomerInfoId", "FirstName", "MiddleName", "LastName", "Address", "PhoneNumber")

	def __init__(self):
		self.m_customerInfoId
		self.m_firstName
		self.m_middleName
		self.m_lastName
		self.m_address
		self.m_phoneNumber

class VirtualCart:

	sc_columnHeaders = ("VirtualCartId", "CustomerInfoFk", "BarcodeDetailsFk", "NumCheckedOut")

	def __init__(self):
		self.m_virtualCartId
		self.m_customerInfoFk
		self.m_barcodeDetailsFk
		self.m_numCheckout