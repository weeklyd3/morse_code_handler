#!/usr/bin/env python3
# Python program to implement Morse Code Translator 

''' 
VARIABLE KEY 
'cipher' -> 'stores the morse translated form of the english string' 
'decipher' -> 'stores the english translated form of the morse string' 
'citext' -> 'stores morse code of a single character' 
'i' -> 'keeps count of the spaces between morse characters' 
'message' -> 'stores the string to be encoded or decoded' 
'''

# Dictionary representing the morse code chart 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
					'C':'-.-.', 'D':'-..', 'E':'.', 
					'F':'..-.', 'G':'--.', 'H':'....', 
					'I':'..', 'J':'.---', 'K':'-.-', 
					'L':'.-..', 'M':'--', 'N':'-.', 
					'O':'---', 'P':'.--.', 'Q':'--.-', 
					'R':'.-.', 'S':'...', 'T':'-', 
					'U':'..-', 'V':'...-', 'W':'.--', 
					'X':'-..-', 'Y':'-.--', 'Z':'--..', 
					'1':'.----', '2':'..---', '3':'...--', 
					'4':'....-', '5':'.....', '6':'-....', 
					'7':'--...', '8':'---..', '9':'----.', 
					'0':'-----', ', ':'--..--', '.':'.-.-.-', 
					'?':'..--..', '/':'-..-.', '-':'-....-', 
					'(':'-.--.', ')':'-.--.-',',':'--..--'} 

# Function to encrypt the string 
# according to the morse code chart 
def encrypt(message): 
	cipher = '' 
	for letter in message: 
		if letter != ' ': 

			# Looks up the dictionary and adds the 
			# correspponding morse code 
			# along with a space to separate 
			# morse codes for different characters 
			cipher += MORSE_CODE_DICT[letter] + ' '
		else: 
			# 1 space indicates different characters 
			# and 2 indicates different words 
			cipher += ' '

	return cipher 

# Function to decrypt the string 
# from morse to english 
def decrypt(message): 

	# extra space added at the end to access the 
	# last morse code 
	message += ' '

	decipher = '' 
	citext = '' 
	for letter in message: 

		# checks for space 
		if (letter != ' '): 

			# counter to keep track of space 
			i = 0

			# storing morse code of a single character 
			citext += letter 

		# in case of space 
		else: 
			# if i = 1 that indicates a new character 
			i += 1

			# if i = 2 that indicates a new word 
			if i == 2 : 

				# adding space to separate words 
				decipher += ' '
			else: 

				# accessing the keys using their values (reverse of encryption) 
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
				.values()).index(citext)] 
				citext = '' 

	return decipher 

# Hard-coded driver function to run the program 
import getpass
x=0
def clear_screen():
	import os
	if os.name=='nt':
		os.system("cls")
	else:
		os.system('clear')
while x==0:
	clear_screen()
	print('All Actions')
	print('=============')
	print("""Options:
	[1] Decrypt Morse Code
	[2] Encrypt Morse Code""")
	action2do=str(input('Enter your choice: '))
	if action2do!='1' and action2do!='2':
		print("Input not allowed. Clearing...")
	if action2do=='1':
		clear_screen()
		print("Decrypt Morse Code to Terminal")
		print("================================")
		print('Morse code to decrypt (in the format of . and - with a space between each letter): ', end=' ')
		msg=str(input())
		try:
			decrypted=decrypt(msg)
			print(decrypted)
			print("The text is shown above. Press Enter to continue.")
		except ValueError:
			print("The morse code is not valid. Press Enter to continue.")
		getpass.getpass(prompt='',stream=None)
	if action2do=='2':
		clear_screen()
		print("Encrypt Morse Code to Terminal")
		print("================================")
		print("Text to encrypt: ", end='')
		msg=input()
		msg1=msg.upper()
		encrypted=encrypt(msg1)
		print(encrypted)
		print("The text is shown above. Press Enter to continue.")
		getpass.getpass(prompt='',stream=None)