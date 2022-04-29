from Em_Ex import *
Stego_Medium = input("Enter StegoMedia Name:")
user_Choice = int(input("1.Embed or 2.Extract"))
if user_Choice == 1 :
	Stego_Message = input("Enter Text to be embedded:")
	msg_Embed(Stego_Medium,Stego_Message)
	print("Message successfully hidden")
elif user_Choice == 2 :
	Stego_Text = msg_Extract(Stego_Medium)
	print("Extracted Message :" +Stego_Text)
	
	