import base64

def hex_to_64( hex ):
	my_hex = base64.b64encode(hex.decode("hex"))
	print my_hex
	return


hex_input = raw_input("gimme a hex value...\n")

hex_to_64(hex_input)