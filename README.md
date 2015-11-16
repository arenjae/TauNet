TauNet
=============
###Connecting Pies together since 2015

TauNet is a simple protocol to send and receive encrypted messages over a private network anywhere in the world.


####Outline
- RC4 <- algorithm to output a stream of random numbers (run key scheduler 20 times after each message received / and transmitted)
- Password (universal for a network) - "password"
- IV thing (10 randomly chosen bytes that are appended to the password)
- Address Book
- Log (to store unsent messages)


####Address Book
| IP Address      | Port  | Name     |
| --------------- | ----- | -------- |
| pi.arenjae.com  | 6283  | Rachael  |
| 131.252.211.245 | 22    | Nathan   |



####Notes
- Scapy (to send a package)
    - search for python socket example

- Need to use threads to continue receiving while sending a message so no message gets lost

#####Basic Code Outline:
- Need an encrypt / decrypt function.
    - Functions will decrypt a message or encrypt a message using protocol specified by Bart
    
- Listen() function for a specific port - any message sent to that port will be received, decrypted, and then displayed to the user
- Send function (EncryptedStringToSend, AddressToSendTo)
    - Function will send an inputted string to an address 
    
- Address Book -should be a class - maybe a list

- Main Screen - should be a class, this should handle the threads to ensure a message is never missed

- Log - should be a class also


#####Advance Code Outline:
 - protocol.py 
 - server.py
 - client.py
 - addressBook.py
 - TauNet.py
    - Main handler for everything. This has a while loop that will keep looping until user decides to quit program
    - It contains the main screen. If the user wants view messages, it calls the server class. If the user wants to send a message, it calls the addressBook class, has the user pick a person, then has the user choose
     
     
     
          import threading

def worker(num):
    """thread worker function"""
    print 'Worker: %s' % num
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()