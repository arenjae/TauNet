import server
import client
import threading
import protocol

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
    serverThread = threading.Thread(target=server.server.startServer(server), args=())

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

        clientThread = threading.Thread(target=client.client.clientStart(client, target, encryptedMessage),
                                        args=(message,))
        # this should be a class that I can send a message and an address too
        # and it will send

        # Replace this line with a server call to display all messages

    elif userChoice == 2:
        print("Viewing messages..")
        # serverThread.viewMessages
    else:
        print("That is not a valid choice...")

    return


addressBookPopulate()
while True:
    MainScreen()
