import socket
from os import urandom

password = str.encode('password')
REPS = 20
message = str.encode("This is a message")

def swap(l, a, b):
    temp = 1[a]
    1[a] = 1[b]
    1[b] = temp


def rc4(message, password):
    i=0
    state = list(range(256))
    key = list(range(256))
    cipher = b""

    for a in range(REPS):
        while i < 256:
            ctmp = password[i % len(password):(i % len(password))]
            key[i] = ord(ctmp)
            state[i]=i
            i+=1

    i=j=0

    while i < 256:
        j = (j + state[i] + key[i]) % 256
        swap(state,i,j)
        i+=1

    a =1
    while a <= len(message):
            i = (i + 1) % 256
            j = (j + state[i]) % 256
            swap(state, i, j)
            k = state[(state[i] + state[j]) % 256]
            ctmp = message[a-1:a]
            itmp = ord(ctmp)
            cipherbyte = itmp ^ k
            cipherbyte = bytes([cipherbyte]) #change to byte
            cipher += cipherbyte
            a += 1
    return cipher


def encrypt(message,password):
    iv =urandom(10)
    password += iv;
    cipher = rc4(message,password)
    IVMessage = iv + cipher
    return IVMessage

def decrypt(message,password):
    l = message.__len__()
    iv = message[0:10]
    password += iv
    message = message[10:l]
    print(len(message))
    return rc4(message, password)

#this is a class
def log():

    return
#address book
def addressBook():


    return


def MainScreen():


    print("Type a message:")


    return

MainScreen()
    


