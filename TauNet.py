# Copyright (C) 2015 Rachael Johnson arenjae.com, email: rj@arenjae.com
# Created with in collaboration with Graham Drakeley, drak2@pdx.edu
# and Nathan Reed natreed@pdx.edu

import server
import client
import threading
import protocol
from os import _exit

password = str.encode('password')
PORT = 6283

addressNames = []
addressList = []
log = []
addressFile = 'addresses.txt'
strFrom = "from: rhatchet\r\n"
strVersion = "version: v0.1\r\n"


# address book
def addressBook():
	for i in range(len(addressNames)):
		print(i + 1, ". ", addressNames[i])
	intTarget = int(input("Choose a person to send a message to: "))
	target = (addressList[intTarget - 1], PORT)

	global strTo
	strTo = "to: " + addressNames[intTarget - 1] + "\r\n"

	return target


# Adds addresses and usernames from addresses.txt to a dictionary
def addressBookPopulate():
	count = 0
	with open(addressFile, 'r') as f:
		addressBook = f.readlines()
	with open(addressFile, 'r') as f:
		for line in f:
			count += 1
	for i in range(count):
		b = addressBook[i].split()
		addressNames.append(b[0])
		addressList.append(b[1])
	addressNames.append('Test')
	addressList.append('localhost')


# Main Screen, user always returns to this screen
def MainScreen():
	print("-----Main Menu------")
	print("What would you like to do?")
	print("1. Send Message")
	print("2. View Messages")
	print("3. Quit")
	print("-----------------")
	userChoice = input(":")

	if userChoice == "1":
		target = addressBook()

		message = input("Type a message:")
		while len(message.encode('utf-8')) > 94:  # restrict message to 94 bytes
			message = input("Message is too long. \nType a message:")

		encryptedMessage = protocol.encrypt(strVersion + strFrom + strTo + message, password)
		clientThread = threading.Thread(target=client.clientFunc, args=(target, encryptedMessage))
		clientThread.start()

	elif userChoice == "2":
		print("Viewing messages..")
		for msg in server.messages:
			print((msg))

	elif userChoice == "3":
		return False

	else:
		print("That is not a valid choice...")

	return True

# This is where the program really starts
serverThread = server.server()
serverThread.start()
addressBookPopulate()

while MainScreen():
	pass

_exit(0)
