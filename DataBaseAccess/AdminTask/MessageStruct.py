class MessageStruct:

	# Message header for communication direction
	cs_Pi2Ard = "P>A"
	cs_Ard2Pi = "P<A"

	# Message header for message content identifier
	cs_RI     = "RI"	# Retrieve Inventory
	cs_DI 	  = "DI"    # Deposit Inventory

	# for acknowledgement byte
	cs_ack    = "ACK"