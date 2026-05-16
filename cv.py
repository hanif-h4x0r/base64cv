import os
import base64
_ = os.system("clear")

def b64_txt():
	teks = input("Enter your base64 : ")
	teks_to_byte = base64.b64decode(teks)
	result = teks_to_byte.decode("utf-8")
	print(result)

def txt_b64():
	teks = input("Enter your text : ")
	teks_to_byte = teks.encode("utf-8")
	change = base64.b64encode(teks_to_byte)
	result = change.decode('utf-8')
	print(result)


print(f"\n=== BASE64 CONVERTER ===\n1. B64 to txt\n2. Txt to B64\n3. Quit\n")

choice = int(input("Choose : "))

while True:

	if choice == 1:
		b64_txt()
	elif choice == 2:
		txt_b64()
	elif choice == 3:
		break
	
