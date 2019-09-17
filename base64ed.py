import base64
import getpass

def encoder():
	userinput = input("Masukan nama file yang akan diencode = ")
	f = open(userinput, "r")
	plaintext = f.read()
	tmp = plaintext.encode("UTF-8")
	n = eval(input("Berapa kali diencode ? "))
	stop = 0;
	for i in range(0, 1):
		for j in range(0, n):
			tmp = base64.b64encode(tmp)
	chipertext = tmp.decode("UTF-8")
	f = open("chipertext.txt", "w")
	f.write(chipertext)
	f.close()
	print("Anda Telah Berhasil MengEncode File Anda")

def decoder():
	userinput = input("Masukan nama file yang akan diencode = ")
	f = open(userinput, "r")
	plaintext = f.read().encode("UTF-8")
	while(True):
		try:
			plaintext = base64.b64decode(plaintext)
		except:
			f = open("plaintext.txt", "w")
			f.write(plaintext.decode("UTF-8"))
			f.close()
			print("Anda Telah Berhasil MenDecode File Anda")
			break
print("-------------------------")
print("Coded by @auliaahmadnabil")
print("-------------------------")
print("\t MENU : ")
print("\n1. Encoder")
print("2. Decoder")
pil = eval(input("Masukan Pilihanmu : "))
if pil == 1:
	encoder()
elif pil == 2:
	decoder()
else:
	print("Pilihamu tidak ada")









