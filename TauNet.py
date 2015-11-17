# Copyright (C) 2015 Rachael Johnson arenjae.com, email: rj@arenjae.com
# Created with in collaboration with Graham Drakeley, drak2@pdx.edu
# and Nathan Reed natreed@pdx.edu

import server
import client
import threading
import protocol
from os import _exit

password = str.encode('password')
addressBookNameList = ("1. Rachael", "2. Nathan", "3. Yourself (for testing purposes")
addressBookAddressList = ('pi.arenjae.com', '131.252.211.245', 'localhost')
log = list()
PORT = 6283


# address book
def addressBook():
    print(addressBookNameList)
    target = (addressBookAddressList[int(input("Choose a person to send a message to: ")) - 1], PORT)

    return target


# In the future this will load a file of addresses/usernames
def addressBookPopulate():
    pass


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
        encryptedMessage = protocol.encrypt(message, password)
        print("Encrypted message: ", encryptedMessage)

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


serverThread = server.server()
serverThread.start()
addressBookPopulate()
while MainScreen():
    pass

_exit(0)