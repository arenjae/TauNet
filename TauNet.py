#import clientScratch
#import serverScratch

import protocol

password = str.encode('password')
addressBookList = list()
log = list()

# address book
def addressBook():
    print(addressBookList)
    choice=input("Choose a person to send a message to: ")

    return choice

def addressBookPopulate():
    addressBookList.append("1. Rachael")
    addressBookList.append("2. Nathan")


def MainScreen():

    #clientScratch #this should be a class that I can send a message and an address too
    #and it will send

    #serverScratch #this should be a class on a separate thread that always receives. When
    #the user wishes to read his messages, call serverScratch.readMessages . Should read
    #messages every time user does something

    print("-----Main Menu------")
    print("What would you like to do?")
    print("1. Send Message")
    print("2. View Messages")
    print("-----------------")
    userChoice = input(":")

    if userChoice == "1":
        addressBook()
        message = input("Type a message:")
        encryptedMessage = protocol.encrypt(message, password)
        print("Encrypted message: ", encryptedMessage)
        print("Decrypted message: ", protocol.decrypt(encryptedMessage, password))

    else:
        #serverScratch.viewMessages
        print("Viewing messages..")

    return


addressBookPopulate()
MainScreen()
