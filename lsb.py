def Do_lsb(msg_bits,frame_bytes):

	for i, bit in enumerate(msg_bits):
		frame_bytes[i] = (frame_bytes[i] & 254) | bit

	return(bytes(frame_bytes))


def Undo_lsb(frame_bytes):
	
	for i in range(len(frame_bytes)):
		frame_bytes[i] = (frame_bytes[i] & 1)
	
	return(frame_bytes)