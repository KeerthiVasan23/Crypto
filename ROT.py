import argparse

parser=argparse.ArgumentParser(
    description='''Encrypt and Decrypt ROT-n Ciphers''')
args=parser.parse_args()

import enchant
option=999
d = enchant.Dict("en_US")
plainText=[]
cipherText=[]

while(option!=0):
	option=int(input("ROT-n Options: 1- Encrypt 2- Decrypt 0- Exit\n"))
	if(option==0):
		break
	elif(option==1):
		plainText=input("Enter Plain Text: ").lower().split()
		n=int(input("n = "))
		print("Cipher Text: ",end="")
		for j in plainText:
			for i in j:
				print(chr(((ord(i)-97+n)%26)+97),end="")
			print(" ",end="")
		print()
	elif(option==2):
		cipherText=input("Enter Cipher Text: ").lower().split()
		force=input("Do you know the cipher? y/n\n")
		if(force=='n'):
			print("Plain Text: ",end="")
			for j in cipherText:
				n=0
				cipher=["emppppty","-lissst"]
				while(d.check(''.join(cipher))!=True and n<26):
					cipher=[]
					for i in j:
						cipher.append(chr(((ord(i)-97-n)%26)+97))
					n+=1
				if(d.check(''.join(cipher))==False):
					print("~err~",end="")
				if(n!=26):
					print(''.join(cipher),end="")
				print(" ",end="")
			print()
		else:
			n=int(input("n = "))
			print("Plain Text: ",end="")
			for j in cipherText:
				for i in j:
					print(chr(((ord(i)-97-n)%26)+97),end="")
				print(" ",end="")
			print()
	des=input("Do you want to continue? y/n\n")
	if(des=='n'):
		print("~Thank You~")
		break
	print()



