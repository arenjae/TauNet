import server
import client
import threading
import protocol

password = str.encode('password')
addressBookList = list()
log = list()
PORT = 6031


# address book
def addressBook():
    print(addressBookList)
    target = input("Choose a person to send a message to: ")

    # Delete this line after addressBook has been properly set up
    target = ('localhost', PORT)
    return target


def addressBookPopulate():
    addressBookList.append("1. Rachael")
    addressBookList.append("2. Nathan")


def MainScreen():
    #serverThread = threading.Thread(target=server.server.startServer(server), args=())

    # this should be a class on a separate thread that always receives. When
    # the user wishes to read his messages, call serverScratch.readMessages . Should read
    # messages every time user does something

    print("-----Main Menu------")
    print("What would you like to do?")
    print("1. Send Message")
    print("2. View Messages")
    print("-----------------")
    userChoice = input(":")

    if userChoice == "1":
        target = addressBook()
        message = input("Type a message:")
        encryptedMessage = protocol.encrypt(message, password)
        print("Encrypted message: ", encryptedMessage)

        clientThread = threading.Thread(target=client.client.clientStart(client, target,encryptedMessage), args=(message,))
        # this should be a class that I can send a message and an address too
        # and it will send

        print("Decrypted message: ", protocol.decrypt(encryptedMessage, password))

    else:
        print("Viewing messages..")
        # serverThread.viewMessages

    return


addressBookPopulate()
MainScreen()
