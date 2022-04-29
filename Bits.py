def into_Bits_Array(string):

	string_bits = ""
	for i in string:
		string_bits = string_bits + bin(ord(i)).lstrip('0b').rjust(8,"0")
	text_msg_bits_array = list(map(int, "".join(string_bits))) 

	return(text_msg_bits_array)
	
def into_String(bytes):

	string_bits = ""
	for i in range(0,len(bytes),8):
		string_bits = string_bits + chr(int("".join(map(str,bytes[i:i+8])),2))
	text_string_bits = "".join(string_bits)
	
	return(text_string_bits)