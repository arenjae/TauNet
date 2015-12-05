# Copyright (C) 2015 Rachael Johnson arenjae.com, email: rj@arenjae.com
# Created with in collaboration with Graham Drakeley, drak2@pdx.edu
# and Nathan Reed natreed@pdx.edu

import server
import client
import threading
import protocol
from os import _exit
import os

password = str.encode('password')
PORT = 6283

addressNames = []
addressList = []
log = list
addressFile = 'addresses.txt'
strFrom = "from: rhatchet\r\n"
strVersion = "version: 0.2\r\n"

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
		for _ in f:
			count += 1
	for i in range(count):
		b = addressBook[i].split()
		addressNames.append(b[0])
		addressList.append(b[1])
	addressNames.append('Test')
	addressList.append('localhost')

def openLog():
	print("Opening Log...")
	if len(client.logTarget) == 0:
		print("\nNo messages in Log")
		return
	for i in range(len(client.logTarget)):
		print(i+1, ".")
		print("To: " + str(client.logTarget[i]))
		print("Message: \n" + client.logMessage[i])
		print("---------------------------")


	userChoice = int(input("Select a log message: "))
	if 0 < userChoice <= len(client.logTarget):
		logMenu(userChoice-1)
	else:
		print("That is not a valid choice, returning to Main Menu...")


def logMenu(i):
	print("---------Log Menu---------")
	print("What would you like to do?")
	print("1. Send Message")
	print("2. Delete Message")
	print("3. Cancel")
	print("--------------------------")

	userChoice = input(": ")
	if userChoice == "1":
		encryptedMessage = protocol.encrypt(strVersion + strFrom + strTo + '\r\n' + client.logMessage[i], password)
		clientThread = threading.Thread(target=client.clientFunc, args=(client.logTarget[i], encryptedMessage))
		clientThread.start()
	elif userChoice == "2":
		del client.logMessage[i]
		del client.logTarget[i]
	elif userChoice == "3":
		return

	else:
		print("That is not a valid choice. Returning to Main Menu..")


# Main Screen, user always returns to this screen
def MainScreen():
	print('{:-^100}'.format("Main Menu"))
	print("What would you like to do?")
	print("1. Send Message")
	print("2. View Messages")
	print("3. View Message from Log")
	print("4. Quit")
	print('{:-^100}'.format(""))
	userChoice = input(":")

	if userChoice == "1":
		target = addressBook()

		os.system('cls' if os.name == 'nt' else 'clear')
		message = input("Type a message:")
		while len(message.encode('utf-8')) > 934:  # restrict message to 934 bytes
			message = input("Message is too long. \nType a message:")

		encryptedMessage = protocol.encrypt(strVersion + strFrom + strTo + '\r\n' + message, password)
		clientThread = threading.Thread(target=client.clientFunc, args=(target, encryptedMessage))
		clientThread.start()

	elif userChoice == "2":
		print("Viewing messages..")
		for msg in server.messages:
			print(msg)

	elif userChoice == "3":
		openLog()

	elif userChoice == "4":
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

print("\nQuiting TauNet...")
_exit(0)
