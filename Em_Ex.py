import wave
from Bits import *
from lsb import *
#linking functions ouside this file
#from a(file) import b,c,d(functions)
#import / import module
#module.function
def msg_Embed(audio_name,text_msg):
	audio = wave.open(audio_name, mode='rb')
	audio_Frames_Bytes = bytearray(list(audio.readframes(audio.getnframes())))
	
	text_msg = text_msg + int((len(audio_Frames_Bytes)/8)-(len(text_msg)*8)) *'@'
	
	text_msg_bits = into_Bits_Array(text_msg)
	
	Frames_with_Msg = Do_lsb(text_msg_bits,audio_Frames_Bytes)
	
	with wave.open("Stego"+audio_name, mode='wb') as sm:
		sm.setparams(audio.getparams())
		sm.writeframes(Frames_with_Msg)
	audio.close()
	
def msg_Extract(audio_name):
	audio = wave.open(audio_name, mode='rb')
	audio_Frames_Bytes = bytearray(list(audio.readframes(audio.getnframes())))
	msg_Bytes = Undo_lsb(audio_Frames_Bytes)
	msg_String = into_String(msg_Bytes)
	msg_Text = msg_String.split("@@@@")[0]
	return(msg_Text)
	audio.close()
	